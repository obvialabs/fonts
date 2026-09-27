"""Validate a manually dispatched npm staged release before any publication.

The release gate binds the requested version to committed package metadata, the
trusted GitHub repository, public access policy, and a clean main-branch checkout.
"""

from __future__ import annotations

import argparse
import re
import subprocess

from tooling import ROOT, fail, package_json, package_version

SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
EXPECTED_REPOSITORY = "git+https://github.com/obvialabs/fonts.git"


# Validate immutable release metadata before the expensive build/package/publish stages.
def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a release dispatch before any build or publish work")
    parser.add_argument("--version", required=True)
    args = parser.parse_args()

    expected = args.version.removeprefix("v")
    actual = package_version()
    if expected != actual:
        fail(f"Requested release {expected} does not match packages/fonts/package.json ({actual})")
    if not SEMVER.fullmatch(actual):
        fail(f"Invalid package version: {actual}")

    package = package_json()
    repository = package.get("repository", {})
    if repository.get("url") != EXPECTED_REPOSITORY:
        fail("package.json repository.url must match the trusted GitHub repository exactly")
    if package.get("name") != "@obvia/fonts":
        fail("Unexpected npm package name")
    if package.get("publishConfig", {}).get("access") != "public":
        fail("@obvia/fonts must explicitly publish with public access")

    status = subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True)
    if status.strip():
        fail("Release working tree is not clean")

    branch = subprocess.check_output(
        ["git", "branch", "--show-current"], cwd=ROOT, text=True
    ).strip()
    # GitHub Actions may check out workflow_dispatch commits detached. Local manual
    # validation is allowed on main only; detached CI is guarded by github.ref.
    if branch and branch != "main":
        fail(f"Release validation must run from main, not {branch}")

    print(f"Release metadata verified for @obvia/fonts@{actual}")


if __name__ == "__main__":
    main()
