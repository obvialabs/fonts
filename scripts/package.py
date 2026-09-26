from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

from tooling import ROOT, fail, package_json, package_version, pnpm_command, remove, require_command, run, sha256

PACKAGE_DIR = ROOT / "packages/fonts"
OUTPUT_DIR = ROOT / "output/npm"
STAGE_DIR = OUTPUT_DIR / ".stage"


def build_wrapper() -> None:
    run(pnpm_command("install", "--frozen-lockfile"), cwd=PACKAGE_DIR)
    run(pnpm_command("run", "build"), cwd=PACKAGE_DIR)


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

    (STAGE_DIR / "package.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    shutil.copy2(PACKAGE_DIR / "readme.md", STAGE_DIR / "README.md")
    shutil.copy2(ROOT / "OFL.txt", STAGE_DIR / "LICENSE.txt")
    shutil.copytree(PACKAGE_DIR / "dist", STAGE_DIR / "dist")


def pack_listing() -> set[str]:
    completed = subprocess.run(
        ["npm", "pack", "--dry-run", "--ignore-scripts", "--json"],
        cwd=STAGE_DIR,
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(completed.stdout)
    if not data:
        fail("npm pack returned no package information")
    return {entry["path"] for entry in data[0].get("files", [])}


def validate_pack_listing(files: set[str]) -> None:
    allowed_roots = ("dist/",)
    allowed_files = {"package.json", "README.md", "LICENSE.txt"}
    unexpected = sorted(
        path for path in files
        if path not in allowed_files and not path.startswith(allowed_roots)
    )
    if unexpected:
        fail("Unexpected files would be published: " + ", ".join(unexpected))

    required = {"dist/index.js", "dist/index.d.ts", "package.json", "LICENSE.txt"}
    missing = required - files
    if missing:
        fail("Required npm files missing: " + ", ".join(sorted(missing)))
    if not any(path.startswith("dist/fonts/") for path in files):
        fail("No font binaries would be included in the npm package")
    print(f"npm dry-run contains {len(files)} files")


def main() -> None:
    require_command("npm")
    build_wrapper()
    create_stage()
    validate_pack_listing(pack_listing())

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for old in OUTPUT_DIR.glob("*.tgz"):
        old.unlink()
    for old in OUTPUT_DIR.glob("*.tgz.sha256"):
        old.unlink()

    run([
        "npm", "pack", "--ignore-scripts", "--pack-destination", str(OUTPUT_DIR.resolve())
    ], cwd=STAGE_DIR)

    tarballs = list(OUTPUT_DIR.glob("*.tgz"))
    if len(tarballs) != 1:
        fail(f"Expected one npm tarball, found {len(tarballs)}")
    tarball = tarballs[0]
    (OUTPUT_DIR / f"{tarball.name}.sha256").write_text(
        f"{sha256(tarball)}  {tarball.name}\n", encoding="utf-8"
    )
    remove(STAGE_DIR)
    print(f"Package ready: {tarball.relative_to(ROOT)} (@obvia/fonts {package_version()})")


if __name__ == "__main__":
    main()
