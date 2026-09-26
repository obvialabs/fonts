from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from tooling import ROOT, fail

SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
PACKAGE_JSON = ROOT / "packages/fonts/package.json"


def main() -> None:
    parser = argparse.ArgumentParser(description="Update @obvia/fonts version for a release PR")
    parser.add_argument("version")
    args = parser.parse_args()
    if not SEMVER.fullmatch(args.version):
        fail(f"Invalid semantic version: {args.version}")

    data = json.loads(PACKAGE_JSON.read_text(encoding="utf-8"))
    old = data["version"]
    if old == args.version:
        fail(f"Package is already version {args.version}")
    data["version"] = args.version
    PACKAGE_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"@obvia/fonts: {old} -> {args.version}")
    print("Review the diff, update changelog.md if needed, then commit this change through a PR.")


if __name__ == "__main__":
    main()
