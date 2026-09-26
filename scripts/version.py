"""Update the npm package version without reformatting package.json.

The repository intentionally keeps a hand-aligned package.json layout. Release
version changes must therefore edit only the existing `version` field instead of
round-tripping the complete document through a JSON serializer.
"""

from __future__ import annotations

import argparse
import json
import re

from tooling import ROOT, fail

SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
PACKAGE_JSON = ROOT / "packages/fonts/package.json"
VERSION_LINE = re.compile(r'(?m)^(\s*"version"\s*:\s*")([^"]+)("\s*,?\s*)$')


def update_version_text(text: str, version: str) -> tuple[str, str]:
    """Return package.json text with only the existing version value changed."""
    match = VERSION_LINE.search(text)
    if not match:
        fail("package.json does not contain a recognizable top-level version field")

    old = match.group(2)
    replacement = f"{match.group(1)}{version}{match.group(3)}"
    return text[: match.start()] + replacement + text[match.end() :], old


def main() -> None:
    """Validate the requested semver and preserve the package manifest layout."""
    parser = argparse.ArgumentParser(
        description="Update @obvia/fonts version for a release PR without reformatting package.json"
    )
    parser.add_argument("version")
    args = parser.parse_args()

    if not SEMVER.fullmatch(args.version):
        fail(f"Invalid semantic version: {args.version}")

    original = PACKAGE_JSON.read_text(encoding="utf-8")

    # Parse first so malformed JSON is rejected before the textual replacement.
    package = json.loads(original)
    if package.get("name") != "@obvia/fonts":
        fail("Unexpected npm package name")

    rendered, old = update_version_text(original, args.version)
    if old == args.version:
        fail(f"Package is already version {args.version}")

    PACKAGE_JSON.write_text(rendered, encoding="utf-8")
    print(f"@obvia/fonts: {old} -> {args.version}")
    print("Review the diff, update changelog.md if needed, then commit this change through a PR.")


if __name__ == "__main__":
    main()
