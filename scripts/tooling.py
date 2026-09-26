"""Shared filesystem, process, hashing, and package helpers for font tooling.

Keeping these primitives in one module makes local commands and GitHub Actions
use the same path handling, failure semantics, integrity calculations, and npm
metadata access.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parents[1]


# Run a required subprocess and preserve its non-zero exit status.
def run(args: Sequence[str], *, cwd: Path | None = None, env: dict[str, str] | None = None) -> None:
    printable = " ".join(str(a) for a in args)
    print(f"+ {printable}")
    subprocess.run(list(args), cwd=cwd or ROOT, env=env, check=True)


# Capture a small textual command result for metadata/integrity helpers.
def capture(args: Sequence[str], *, cwd: Path | None = None) -> str:
    return subprocess.check_output(list(args), cwd=cwd or ROOT, text=True).strip()


# Fail early with a useful message when a required external tool is unavailable.
def require_command(name: str) -> str:
    path = shutil.which(name)
    if not path:
        fail(f"Required command not found: {name}")
    return path


# Remove generated files/directories while handling symlinks safely.
def remove(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
    elif path.exists():
        shutil.rmtree(path)


# Atomically-ish swap a complete generated tree while retaining rollback on failure.
def replace_tree(source: Path, destination: Path) -> None:
    """Replace a generated directory only after its replacement is complete."""
    if not source.is_dir():
        fail(f"Generated directory is missing: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    backup = destination.with_name(f".{destination.name}.previous")
    remove(backup)
    if destination.exists():
        destination.rename(backup)
    try:
        source.rename(destination)
    except Exception:
        if backup.exists() and not destination.exists():
            backup.rename(destination)
        raise
    else:
        remove(backup)


# Stream files when hashing so large font/release artifacts do not need full buffering.
def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


# Hash both relative paths and bytes for deterministic build-input freshness checks.
def digest_paths(paths: Iterable[Path]) -> str:
    digest = hashlib.sha256()
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(p for p in path.rglob("*") if p.is_file())
        elif path.is_file():
            files.append(path)
    for path in sorted(set(files), key=lambda p: p.relative_to(ROOT).as_posix()):
        relative = path.relative_to(ROOT).as_posix().encode("utf-8")
        digest.update(len(relative).to_bytes(4, "big"))
        digest.update(relative)
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    return digest.hexdigest()


# Centralize the committed inputs that define whether generated font outputs are stale.
def build_input_digest() -> str:
    return digest_paths([
        ROOT / "sources",
        ROOT / "requirements.txt",
        ROOT / ".python-version",
        ROOT / "scripts/build.py",
        ROOT / "scripts/tooling.py",
    ])


# Write machine-generated JSON deterministically for stable review/debug output.
def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


# Yield supported generated font binaries in a deterministic order.
def iter_font_files(root: Path) -> Iterable[Path]:
    for suffix in ("*.ttf", "*.otf", "*.woff2"):
        yield from sorted(root.rglob(suffix))


# Capture source revision when Git is available; keep local/exported builds functional.
def git_sha() -> str:
    try:
        return capture(["git", "rev-parse", "HEAD"])
    except Exception:
        return "unknown"


# Read the canonical npm package manifest used by build and release checks.
def package_json() -> dict:
    return json.loads((ROOT / "packages/fonts/package.json").read_text(encoding="utf-8"))


# Return the committed npm version without duplicating manifest parsing logic.
def package_version() -> str:
    return str(package_json()["version"])


# Use Bun for package installation, wrapper compilation, and tarball creation.
def bun_command(*args: str) -> list[str]:
    if shutil.which("bun"):
        return ["bun", *args]
    fail("Bun is required for npm package work. Install Bun 1.4.2 or newer.")


# Emit consistent command-line failures for local runs and GitHub Actions annotations.
def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)
