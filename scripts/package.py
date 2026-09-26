"""Create the inspectable npm release tarball from already validated artifacts.

Packaging compiles the TypeScript wrapper, stages only publishable files, checks
the package allow-list, and emits one checksummed .tgz. Development tooling
and lifecycle scripts are deliberately removed from the staged manifest.
"""

from __future__ import annotations

import json
import shutil
import tarfile
from pathlib import Path

from tooling import ROOT, bun_command, fail, package_json, package_version, remove, require_command, run, sha256

PACKAGE_DIR = ROOT / "packages/fonts"
OUTPUT_DIR = ROOT / "output/npm"
STAGE_DIR = OUTPUT_DIR / ".stage"


# Compile the TypeScript wrapper with the repository-selected Bun toolchain.
def build_wrapper() -> None:
    run(bun_command("install", "--frozen-lockfile"), cwd=PACKAGE_DIR)
    run(bun_command("run", "build"), cwd=PACKAGE_DIR)


# Build a minimal publication directory rather than packing the repository tree.
def create_stage() -> None:
    remove(STAGE_DIR)
    STAGE_DIR.mkdir(parents=True, exist_ok=True)

    manifest = package_json()
    # Published tarballs never need development tooling or lifecycle scripts.
    # Removing them also ensures packing/staging the already-tested tarball cannot
    # execute repository-local build scripts unexpectedly.
    manifest.pop("devDependencies", None)
    manifest.pop("scripts", None)
    manifest.pop("packageManager", None)
    # The staged manifest explicitly retains the font license alongside dist/.
    # npm includes license.md automatically, while the bundled fonts remain OFL.
    manifest["files"] = ["dist", "LICENSE-OFL.txt"]

    (STAGE_DIR / "package.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    # Keep the package wrapper license and the font license side-by-side.
    # The MIT file applies to the package software; OFL.txt remains with the
    # bundled font binaries and must not be discarded during publication.
    shutil.copy2(PACKAGE_DIR / "readme.md", STAGE_DIR / "README.md")
    shutil.copy2(PACKAGE_DIR / "license.md", STAGE_DIR / "license.md")
    shutil.copy2(ROOT / "OFL.txt", STAGE_DIR / "LICENSE-OFL.txt")
    shutil.copytree(PACKAGE_DIR / "dist", STAGE_DIR / "dist")


# Read the exact contents of the tarball produced by Bun.
def tarball_listing(path: Path) -> set[str]:
    with tarfile.open(path, "r:gz") as archive:
        files = set()
        for member in archive.getmembers():
            if not member.isfile():
                continue
            name = member.name.removeprefix("package/")
            files.add(name)
        return files


# Reject accidental publication of source, cache, credential, or development files.
def validate_pack_listing(files: set[str]) -> None:
    allowed_roots = ("dist/",)
    allowed_files = {"package.json", "README.md", "license.md", "LICENSE-OFL.txt"}
    unexpected = sorted(
        path for path in files
        if path not in allowed_files and not path.startswith(allowed_roots)
    )
    if unexpected:
        fail("Unexpected files would be published: " + ", ".join(unexpected))

    required = {"dist/index.js", "dist/index.d.ts", "package.json", "license.md", "LICENSE-OFL.txt"}
    missing = required - files
    if missing:
        fail("Required npm files missing: " + ", ".join(sorted(missing)))
    if not any(path.startswith("dist/fonts/") for path in files):
        fail("No font binaries would be included in the npm package")
    print(f"Package tarball contains {len(files)} files")


# Produce one checksummed tarball that can be reviewed and staged unchanged.
def main() -> None:
    require_command("bun")
    build_wrapper()
    create_stage()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for old in OUTPUT_DIR.glob("*.tgz"):
        old.unlink()
    for old in OUTPUT_DIR.glob("*.tgz.sha256"):
        old.unlink()

    filename = f"obvia-fonts-{package_version()}.tgz"
    staged_tarball = STAGE_DIR / filename
    run(bun_command("pm", "pack", "--ignore-scripts", "--filename", filename), cwd=STAGE_DIR)
    validate_pack_listing(tarball_listing(staged_tarball))
    tarball = OUTPUT_DIR / filename
    shutil.move(staged_tarball, tarball)
    (OUTPUT_DIR / f"{tarball.name}.sha256").write_text(
        f"{sha256(tarball)}  {tarball.name}\n", encoding="utf-8"
    )
    remove(STAGE_DIR)
    print(f"Package ready: {tarball.relative_to(ROOT)} (@obvia/fonts {package_version()})")


if __name__ == "__main__":
    main()
