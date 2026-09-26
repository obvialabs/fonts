"""Validate generated Obvia font artifacts and release-quality invariants.

Fast checks validate build freshness, OpenType readability, required codepoints,
family coverage parity, and npm distribution layout. Full checks additionally
run Fontspector with FAIL results treated as blocking quality-gate failures.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from fontTools.ttLib import TTFont

from tooling import ROOT, build_input_digest, fail, iter_font_files, package_version, run, sha256

EXPECTED_NPM_FONTS = [
    "packages/fonts/dist/fonts/obvia-sans/Obvia-Variable.woff2",
    "packages/fonts/dist/fonts/obvia-mono/ObviaMono-Variable.woff2",
    "packages/fonts/dist/fonts/obvia-pixel/ObviaPixel-Square.woff2",
    "packages/fonts/dist/fonts/obvia-pixel/ObviaPixel-Grid.woff2",
    "packages/fonts/dist/fonts/obvia-pixel/ObviaPixel-Circle.woff2",
    "packages/fonts/dist/fonts/obvia-pixel/ObviaPixel-Triangle.woff2",
    "packages/fonts/dist/fonts/obvia-pixel/ObviaPixel-Line.woff2",
]


# Ensure generated artifacts still correspond to the current committed inputs.
def validate_manifest() -> None:
    path = ROOT / "output/build-manifest.json"
    if not path.is_file():
        fail("Build manifest missing. Run `make build` first.")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("build_input_sha256") != build_input_digest():
        fail("Build outputs are stale: source/tooling inputs changed after the last build.")
    if manifest.get("package_version") != package_version():
        fail("Build outputs are stale: package version changed after the last build.")

    release = manifest.get("release_zip", {})
    release_path = ROOT / str(release.get("path", ""))
    if not release_path.is_file() or sha256(release_path) != release.get("sha256"):
        fail("Release ZIP does not match the build manifest.")


# Perform inexpensive binary-level invariants before the heavier Fontspector run.
def validate_font(path: Path) -> None:
    try:
        font = TTFont(path, lazy=False)
    except Exception as exc:
        fail(f"Could not parse {path.relative_to(ROOT)}: {exc}")

    if "name" not in font or "cmap" not in font:
        fail(f"Required OpenType tables missing in {path.relative_to(ROOT)}")

    cmap = font.getBestCmap() or {}
    for codepoint in (0x2028, 0x2029):
        if codepoint not in cmap:
            fail(f"U+{codepoint:04X} missing from {path.relative_to(ROOT)}")

    if "variable" in path.parts and "fvar" not in font:
        fail(f"Variable font has no fvar table: {path.relative_to(ROOT)}")

    if path.name.startswith("ObviaMono-Italic") and 0x2107 not in cmap:
        fail(f"U+2107 missing from {path.relative_to(ROOT)}")


# Read the effective Unicode cmap used for family coverage comparisons.
def font_codepoints(path: Path) -> set[int]:
    font = TTFont(path, lazy=False)
    return set((font.getBestCmap() or {}).keys())


# Upright and italic variable fonts must expose the same public Unicode coverage.
def validate_family_codepoint_parity() -> None:
    pairs = [
        (
            ROOT / "fonts/Obvia/variable/Obvia[wght].ttf",
            ROOT / "fonts/Obvia/variable/Obvia-Italic[wght].ttf",
        ),
        (
            ROOT / "fonts/ObviaMono/variable/ObviaMono[wght].ttf",
            ROOT / "fonts/ObviaMono/variable/ObviaMono-Italic[wght].ttf",
        ),
    ]

    for upright, italic in pairs:
        if not upright.is_file() or not italic.is_file():
            continue
        upright_codepoints = font_codepoints(upright)
        italic_codepoints = font_codepoints(italic)
        if upright_codepoints == italic_codepoints:
            continue

        upright_only = sorted(upright_codepoints - italic_codepoints)
        italic_only = sorted(italic_codepoints - upright_codepoints)
        details = []
        if upright_only:
            details.append(
                "upright-only: " + ", ".join(f"U+{codepoint:04X}" for codepoint in upright_only)
            )
        if italic_only:
            details.append(
                "italic-only: " + ", ".join(f"U+{codepoint:04X}" for codepoint in italic_only)
            )
        fail(
            f"Variable-family codepoint coverage diverges for {upright.parent.parent.name}: "
            + "; ".join(details)
        )

    print("Validated variable-family codepoint parity")


# Validate every generated TTF/OTF/WOFF2 that fontTools can inspect.
def validate_binaries() -> None:
    fonts = list(iter_font_files(ROOT / "fonts"))
    if not fonts:
        fail("No built fonts found. Run `make build` first.")
    for path in fonts:
        validate_font(path)
    validate_family_codepoint_parity()
    print(f"Validated {len(fonts)} font binaries")


# Guard the npm wrapper contract expected by consumers and CSS exports.
def validate_npm_dist() -> None:
    for relative in EXPECTED_NPM_FONTS:
        if not (ROOT / relative).is_file():
            fail(f"Missing npm font artifact: {relative}")
    print("Validated npm font distribution layout")


# Run release-grade Google Fonts profile checks and persist human-readable reports.
def run_fontspector() -> None:
    if not shutil.which("fontspector"):
        fail("fontspector is required for full QA. Install it with `cargo install fontspector`.")

    groups = [
        ("ObviaVF", ROOT / "fonts/Obvia/variable"),
        ("Obvia", ROOT / "fonts/Obvia/ttf"),
        ("ObviaMonoVF", ROOT / "fonts/ObviaMono/variable"),
        ("ObviaMono", ROOT / "fonts/ObviaMono/ttf"),
        ("ObviaPixel", ROOT / "fonts/ObviaPixel/ttf"),
    ]
    report_dir = ROOT / "output/fontspector"
    badge_dir = ROOT / "output/badges"
    report_dir.mkdir(parents=True, exist_ok=True)
    badge_dir.mkdir(parents=True, exist_ok=True)

    for name, directory in groups:
        inputs = list(iter_font_files(directory)) if directory.exists() else []
        if not inputs:
            continue
        run([
            "fontspector",
            "--profile", "googlefonts",
            "--skip-network",
            "--error-code-on", "fail",
            "--loglevel", "warn",
            "--full-lists",
            "--succinct",
            "--html", str(report_dir / f"{name}-fontspector-report.html"),
            "--ghmarkdown", str(report_dir / f"{name}-fontspector-report.md"),
            "--badges", str(badge_dir),
            *[str(path) for path in inputs],
        ])


# Execute fast checks by default; --full adds blocking Fontspector QA.
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true", help="also run blocking Fontspector QA")
    args = parser.parse_args()

    validate_manifest()
    validate_binaries()
    validate_npm_dist()
    if args.full:
        run_fontspector()
    print("Checks passed")


if __name__ == "__main__":
    main()
