"""Build Obvia font families and publish generated artifacts atomically.

The builder validates Glyphs Package sources first, redirects gftools output into
a temporary staging tree, prepares npm font assets and a deterministic release
ZIP, and only replaces the last known-good generated outputs after every step
succeeds.
"""

from __future__ import annotations

import os
import re
import shutil
import zipfile
from pathlib import Path

import glyphsLib

from tooling import (
    ROOT,
    build_input_digest,
    git_sha,
    iter_font_files,
    package_version,
    remove,
    replace_tree,
    require_command,
    run,
    sha256,
    write_json,
)

FONT_FAMILIES = {
    "Obvia": "obvia-sans",
    "ObviaMono": "obvia-mono",
    "ObviaPixel": "obvia-pixel",
}

# Only normalize variable-font names for the npm API. Static style names are kept
# exactly as generated from the sources (ExtraLight/ExtraBold, etc.).
RENAME_MAP = {
    "Obvia[wght].ttf": "Obvia-Variable.ttf",
    "Obvia[wght].woff2": "Obvia-Variable.woff2",
    "Obvia-Italic[wght].ttf": "Obvia-Italic-Variable.ttf",
    "Obvia-Italic[wght].woff2": "Obvia-Italic-Variable.woff2",
    "ObviaMono[wght].ttf": "ObviaMono-Variable.ttf",
    "ObviaMono[wght].woff2": "ObviaMono-Variable.woff2",
    "ObviaMono-Italic[wght].ttf": "ObviaMono-Italic-Variable.ttf",
    "ObviaMono-Italic[wght].woff2": "ObviaMono-Italic-Variable.woff2",
}

OUTPUT_DIR_RE = re.compile(r"(?m)^outputDir:\s*(.+?)\s*$")


# Source preflight: reject malformed Glyphs Package metadata before invoking gftools.
def validate_source_packages() -> None:
    packages = sorted((ROOT / "sources").glob("*.glyphspackage"))
    if not packages:
        raise SystemExit("No sources/*.glyphspackage directories found")

    for package in packages:
        try:
            glyphsLib.load(package)
        except Exception as exc:
            raise SystemExit(
                f"Invalid Glyphs package {package.relative_to(ROOT)}: {exc}"
            ) from exc

    print(f"Validated {len(packages)} Glyphs source packages")


# Build configs are rewritten temporarily so failed builds never mutate committed configs.
def staged_config(config: Path, stage_fonts: Path) -> Path:
    text = config.read_text(encoding="utf-8")
    match = OUTPUT_DIR_RE.search(text)
    if not match:
        raise SystemExit(f"outputDir missing from {config.relative_to(ROOT)}")

    configured = match.group(1).strip().strip('"\'')
    family_dir = Path(configured).name
    output = (stage_fonts / family_dir).resolve()
    relative_output = os.path.relpath(output, config.parent.resolve()).replace(os.sep, "/")
    rendered = OUTPUT_DIR_RE.sub(f"outputDir: {relative_output}", text, count=1)

    temporary = config.with_name(f".{config.stem}.build.yaml")
    temporary.write_text(rendered, encoding="utf-8")
    return temporary


# Compile every configured family into the isolated build staging tree.
def build_sources(stage_fonts: Path) -> None:
    configs = sorted((ROOT / "sources").glob("config*.yaml"))
    if not configs:
        raise SystemExit("No sources/config*.yaml files found")

    for config in configs:
        temporary = staged_config(config, stage_fonts)
        try:
            run(["gftools", "builder", str(temporary.relative_to(ROOT))])
        finally:
            temporary.unlink(missing_ok=True)


# Copy only distributable font binaries into the npm wrapper layout.
def copy_npm_fonts(source_fonts: Path, target_root: Path) -> None:
    remove(target_root)

    for family, package_dir in FONT_FAMILIES.items():
        source = source_fonts / family
        target = target_root / package_dir
        target.mkdir(parents=True, exist_ok=True)
        for subdir in ("ttf", "webfonts", "variable"):
            src_dir = source / subdir
            if not src_dir.exists():
                continue
            for font in iter_font_files(src_dir):
                if font.parent != src_dir:
                    continue
                name = RENAME_MAP.get(font.name, font.name)
                shutil.copy2(font, target / name)


# Produce a deterministic end-user ZIP and an internal SHA-256 manifest.
def create_release_zip(source_fonts: Path, release_parent: Path) -> Path:
    release_root = release_parent / "obvia-font"
    remove(release_parent)
    release_root.mkdir(parents=True, exist_ok=True)

    for item in source_fonts.iterdir():
        destination = release_root / item.name
        if item.is_dir():
            shutil.copytree(item, destination)
        else:
            shutil.copy2(item, destination)

    optional_files = [
        (ROOT / "docs/DESCRIPTION.en_us.html", release_root / "DESCRIPTION.en_us.html"),
        (ROOT / "docs/article/ARTICLE.en_us.html", release_root / "ARTICLE.en_us.html"),
    ]
    for source, destination in optional_files:
        if source.exists():
            shutil.copy2(source, destination)

    assets = ROOT / "docs/assets"
    if assets.exists():
        shutil.copytree(assets, release_root / "assets")
    shutil.copy2(ROOT / "OFL.txt", release_root / "OFL.txt")

    sums = []
    for file in sorted(p for p in release_root.rglob("*") if p.is_file()):
        if file.name == "SHA256SUMS.txt":
            continue
        sums.append(f"{sha256(file)}  {file.relative_to(release_root).as_posix()}")
    (release_root / "SHA256SUMS.txt").write_text("\n".join(sums) + "\n", encoding="utf-8")

    zip_path = release_parent / "obvia-font.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for file in sorted(p for p in release_root.rglob("*") if p.is_file()):
            arcname = (Path("obvia-font") / file.relative_to(release_root)).as_posix()
            info = zipfile.ZipInfo(arcname, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            with file.open("rb") as handle:
                archive.writestr(info, handle.read(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return zip_path


# Record build inputs and artifact hashes so later checks can detect stale output.
def build_manifest(source_fonts: Path, zip_path: Path) -> dict:
    fonts = []
    for font in iter_font_files(source_fonts):
        fonts.append({
            "path": (Path("fonts") / font.relative_to(source_fonts)).as_posix(),
            "sha256": sha256(font),
            "size": font.stat().st_size,
        })
    return {
        "schema": 1,
        "git_sha": git_sha(),
        "package_version": package_version(),
        "build_input_sha256": build_input_digest(),
        "release_zip": {
            "path": "output/release/obvia-font.zip",
            "sha256": sha256(zip_path),
            "size": zip_path.stat().st_size,
        },
        "fonts": fonts,
    }


# Orchestrate the complete staged build and publish generated trees atomically.
def main() -> None:
    require_command("gftools")
    validate_source_packages()

    work_root = ROOT / "output/.build-work"
    stage_fonts = work_root / "fonts"
    stage_package_fonts = work_root / "package-fonts"
    stage_release = work_root / "release"
    remove(work_root)
    stage_fonts.mkdir(parents=True, exist_ok=True)

    try:
        build_sources(stage_fonts)
        built_fonts = list(iter_font_files(stage_fonts))
        if not built_fonts:
            raise SystemExit("Build produced no font files")

        copy_npm_fonts(stage_fonts, stage_package_fonts)
        zip_path = create_release_zip(stage_fonts, stage_release)
        manifest = build_manifest(stage_fonts, zip_path)

        # Publish generated trees only after every source family and release artifact
        # has been produced successfully. A failed build leaves the last good build intact.
        replace_tree(stage_fonts, ROOT / "fonts")
        replace_tree(stage_package_fonts, ROOT / "packages/fonts/dist/fonts")
        replace_tree(stage_release, ROOT / "output/release")
        write_json(ROOT / "output/build-manifest.json", manifest)
    finally:
        remove(work_root)

    print(f"Build complete: {len(built_fonts)} font files")
    print("Release bundle: output/release/obvia-font.zip")


if __name__ == "__main__":
    main()
