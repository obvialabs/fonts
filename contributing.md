# Contributing to Obvia Fonts

Thanks for contributing to Obvia Fonts. Keep changes focused, build from source, and run the checks before opening a pull request.

## Requirements

You need:

- Git
- [uv](https://docs.astral.sh/uv/)
- Bun 1.4.2+
- GNU Make
- Fontspector for full QA
- Glyphs on macOS if you want to edit the font sources visually

Python 3.11 is managed by `uv`; you do not need a global Python environment for this repository.

## Setup

Clone the repository and run:

```sh
make setup
make build
```

### Windows

WSL2 is the recommended environment because the build scripts and Makefile match Linux CI.

```powershell
wsl --install
```

Inside WSL, install the system tools you need, clone the repository, then use the same commands as Linux. You can still edit the files from Windows or VS Code.

### Linux

Install the native font build dependencies first. On Ubuntu/Debian:

```sh
sudo apt update
sudo apt install -y make ttfautohint libcairo2-dev python3-cairo-dev pkg-config python3-dev
```

Install `uv` and Bun, then:

```sh
make setup
make build
```

### macOS

Install the command-line tools and dependencies with Homebrew:

```sh
xcode-select --install
brew install make ttfautohint cairo pkg-config uv bun
```

Then run:

```sh
make setup
make build
```

Glyphs is recommended for editing `.glyphspackage` sources.

## Repository structure

- `sources/` — editable Glyphs sources and build configs
- `fonts/` — generated font binaries
- `packages/fonts/` — `@obvia/fonts` package source
- `scripts/` — build, QA, packaging, and release helpers
- `output/` — reports and local release artifacts

Do not edit generated font binaries by hand. Change the source, then rebuild.

## Editing fonts

Open the matching source under `sources/` and make the smallest change needed. When adding or changing glyphs, check Unicode values, masters, components, anchors, kerning, and export state. Upright and italic variable families should keep matching public Unicode coverage.

After editing:

```sh
make build
make check
```

For release-quality validation:

```sh
make check-full
```

Fontspector warnings are reported for review. FAIL results block the quality workflow. One Google Fonts check, `googlefonts/repo/dirname_matches_nameid_1`, is excluded because this repository does not use the `google/fonts` repository directory layout.

## npm package

The package is managed with Bun. Generated `dist/` files are not committed.

To build the package locally:

```sh
cd packages/fonts
bun install --frozen-lockfile
bun run build
```

To build fonts, run full QA, and create the publishable tarball in one command:

```sh
make package
```

The resulting `.tgz` is written under `output/npm/`.

## Versioning

Prepare a release version with:

```sh
make version VERSION=1.4.0
```

This updates only the `version` field in `packages/fonts/package.json` and preserves the existing formatting.

Publishing is not automatic when a pull request is merged. The `publish / fonts` workflow is started manually from `main` and stages the tested tarball on npm for final approval. See [`docs/RELEASING.md`](docs/RELEASING.md).

## Pull requests

Before opening a PR:

```sh
make check-full
git diff --check
```

Keep generated caches and package output out of commits. Use scoped Conventional Commits, for example:

```text
fix(fonts): correct italic glyph coverage
build(fonts): improve package tooling
docs(fonts): simplify contribution guide
```

The GitHub checks are split into:

- `build / fonts`
- `quality / fonts`
- `package / fonts`
- `publish / fonts`
- `deploy / fonts`

If a check fails, read the uploaded Fontspector or package artifact before changing the source.

## License

Font files are licensed under the SIL Open Font License 1.1 in [`OFL.txt`](OFL.txt). The npm package wrapper also contains its own `packages/fonts/license.md`; keep the scope of those licenses clear when changing package contents.
