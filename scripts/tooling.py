from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parents[1]


def run(args: Sequence[str], *, cwd: Path | None = None, env: dict[str, str] | None = None) -> None:
    printable = " ".join(str(a) for a in args)
    print(f"+ {printable}")
    subprocess.run(list(args), cwd=cwd or ROOT, env=env, check=True)


def capture(args: Sequence[str], *, cwd: Path | None = None) -> str:
    return subprocess.check_output(list(args), cwd=cwd or ROOT, text=True).strip()


def require_command(name: str) -> str:
    path = shutil.which(name)
    if not path:
        fail(f"Required command not found: {name}")
    return path


def remove(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
    elif path.exists():
        shutil.rmtree(path)


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


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


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


def build_input_digest() -> str:
    return digest_paths([
        ROOT / "sources",
        ROOT / "requirements.txt",
        ROOT / ".python-version",
        ROOT / "scripts/build.py",
        ROOT / "scripts/tooling.py",
    ])


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def iter_font_files(root: Path) -> Iterable[Path]:
    for suffix in ("*.ttf", "*.otf", "*.woff2"):
        yield from sorted(root.rglob(suffix))


def git_sha() -> str:
    try:
        return capture(["git", "rev-parse", "HEAD"])
    except Exception:
        return "unknown"


def package_json() -> dict:
    return json.loads((ROOT / "packages/fonts/package.json").read_text(encoding="utf-8"))


def package_version() -> str:
    return str(package_json()["version"])


def pnpm_command(*args: str) -> list[str]:
    if shutil.which("corepack"):
        return ["corepack", "pnpm", *args]
    if shutil.which("pnpm"):
        return ["pnpm", *args]
    fail("pnpm is required. Install Node.js/Corepack or pnpm before packaging.")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)
