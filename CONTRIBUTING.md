# Contributing to Obvia Fonts

Thank you for contributing to Obvia Fonts. This repository contains the canonical editable sources, build configuration, generated font binaries, QA output, specimen assets, and the unified npm package for the Obvia Sans, Obvia Mono, and Obvia Pixel families.

This guide is intentionally end-to-end. It explains how to prepare a development environment, edit the font sources safely, build on Windows, Linux, and macOS, run quality checks, review generated output, and prepare a pull request without accidentally committing unrelated generated or line-ending changes.

## Repository map

The most important paths are:

- `sources/Obvia.glyphspackage` — Obvia Sans upright masters.
- `sources/Obvia-Italic.glyphspackage` — Obvia Sans italic masters.
- `sources/ObviaMono.glyphspackage` — Obvia Mono upright masters.
- `sources/ObviaMono-Italic.glyphspackage` — Obvia Mono italic masters.
- `sources/ObviaPixel.glyphspackage` — Obvia Pixel source.
- `sources/config-*.yaml` — `gftools builder` configuration for each family.
- `fonts/` — generated distributable fonts. Do not edit these by hand.
- `output/` — generated QA and proofing output. Do not treat these files as source material.
- `scripts/` — repository maintenance/build helper scripts.
- `packages/fonts/` — the `@obvia/fonts` npm package.
- `Makefile` — canonical local build/test/proof entry points.
- `.github/workflows/build.yaml` — CI build and QA reference environment.

The canonical design sources are the files under `sources/*.glyphspackage`. Generated TTF, WOFF2, variable-font, proof, and report files must never be used as the authoritative place to make a design change.

## Supported development environment

CI currently builds with Python 3.11 on Ubuntu. Python 3.11 is therefore the recommended local version even when a newer Python version also works.

The build toolchain includes:

- Python 3.11 and `venv`.
- GNU Make and a POSIX-compatible shell.
- `gftools`, `fontmake`, `fontTools`, `diffenator2`, and the other pinned Python dependencies in `requirements.txt`.
- `ttfautohint` and Cairo development libraries.
- `fontspector` for repository QA.
- Git.
- ZIP utilities used by the release bundle target.
- Node.js and pnpm only when working on `packages/fonts` or release packaging.

Run commands from the repository root unless a section explicitly says otherwise.

## Clone and create a branch

```bash
git clone https://github.com/obvialabs/fonts.git
cd fonts
git switch -c <type>/<short-description>
```

Use a focused branch. Examples:

```text
fix/mono-codepoint-coverage
fix/ligature-carets
feat/latin-glyph-extension
docs/contribution-guide
```

Before editing, verify that the worktree is clean:

```bash
git status --short
```

### Line endings

The source tree is expected to be reviewed by content, not by platform-specific CRLF/LF rewrites. If Git shows thousands of modified files immediately after checkout, first check whether the apparent changes are only line endings. Do not commit a repository-wide line-ending rewrite as part of an unrelated font change.

Useful checks:

```bash
git diff --ignore-space-at-eol --stat
git diff --ignore-space-at-eol
```

If the checkout contains no real local work and the files only changed because of line-ending conversion, restore the worktree before starting:

```bash
git reset --hard HEAD
```

Never run that command when you have uncommitted work you need to keep.

# Platform setup

## Windows

### Recommended: WSL2

The repository Makefile uses POSIX commands and paths such as `venv/bin/activate`, `rm`, `cp`, `find`, and shell loops. The supported and least surprising Windows workflow is therefore **WSL2 with Ubuntu**, rather than running the Makefile directly in PowerShell or `cmd.exe`.

Install WSL from an elevated PowerShell session:

```powershell
wsl --install -d Ubuntu
```

Restart Windows if requested, launch Ubuntu, then install the build prerequisites inside WSL:

```bash
sudo apt update
sudo apt install -y \
  git make zip build-essential \
  python3 python3-venv python3-dev \
  ttfautohint libcairo2-dev python3-cairo-dev pkg-config \
  curl
```

CI uses Python 3.11. If the Ubuntu release installed in WSL does not provide Python 3.11 as its default Python, use `pyenv` or another trusted Python version manager to install 3.11 and create the virtual environment with that interpreter.

Install Rust/Cargo if you want to run Fontspector locally, then install Fontspector:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
cargo install fontspector
```

Clone the repository **inside the Linux filesystem** (for example under `~/src`) for better filesystem performance than building from `/mnt/c/...`:

```bash
mkdir -p ~/src
cd ~/src
git clone https://github.com/obvialabs/fonts.git
cd fonts
```

Build:

```bash
make build
```

Run QA:

```bash
make test
```

Generate proof documents:

```bash
make proof
```

### Editing on Windows

The canonical source format is Glyphs Package (`.glyphspackage`). Glyphs itself is a macOS application. On Windows:

- Metadata, build configuration, scripts, documentation, and carefully scoped textual source changes can be edited with VS Code or another text editor.
- Do not hand-edit outline node coordinates unless you fully understand the Glyphs Package format and interpolation requirements.
- Do not convert the canonical sources to another editor's format and commit a round-trip conversion unless the PR is explicitly about a source-format migration. Such conversions can lose anchors, components, kerning classes, custom parameters, layer metadata, or interpolation information.
- For outline/design work, use a tool that is demonstrably able to preserve the repository's Glyphs Package data, or coordinate the visual source edit from Glyphs on macOS.

You can use VS Code on Windows with the WSL extension so the editor UI runs on Windows while Git, Python, Make, and the source tree remain inside WSL.

## Linux

On Debian/Ubuntu-based distributions:

```bash
sudo apt update
sudo apt install -y \
  git make zip build-essential \
  python3 python3-venv python3-dev \
  ttfautohint libcairo2-dev python3-cairo-dev pkg-config \
  curl
```

CI uses Python 3.11. When your distribution ships another default version, install Python 3.11 through your distribution, `pyenv`, or another trusted version manager and use it for the environment.

For Fontspector:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
cargo install fontspector
```

Then:

```bash
git clone https://github.com/obvialabs/fonts.git
cd fonts
make build
make test
make proof
```

### Editing on Linux

Linux contributors can safely work on build configuration, scripts, documentation, QA fixes, metadata, and source properties stored in the Glyphs Package text files. For visual outline work, use an editor only when it preserves all Glyphs Package semantics used by this repository. Avoid destructive format round trips.

After any source edit, build all families rather than only inspecting the text file. Many source problems are visible only after interpolation and OpenType feature compilation.

## macOS

Install Xcode Command Line Tools:

```bash
xcode-select --install
```

With Homebrew:

```bash
brew install python@3.11 make pkg-config cairo ttfautohint git rust
```

Ensure Python 3.11 is available in your shell. Depending on Homebrew configuration:

```bash
python3.11 --version
```

Install Fontspector:

```bash
cargo install fontspector
```

Clone and build:

```bash
git clone https://github.com/obvialabs/fonts.git
cd fonts
make build
make test
make proof
```

### Editing on macOS with Glyphs

Glyphs 3 is the preferred visual editor for the `.glyphspackage` sources.

Open the required package directly, for example:

```text
sources/Obvia.glyphspackage
sources/Obvia-Italic.glyphspackage
sources/ObviaMono.glyphspackage
sources/ObviaMono-Italic.glyphspackage
sources/ObviaPixel.glyphspackage
```

Save in Glyphs Package format. Do not export binaries from Glyphs and copy them over the repository outputs as a substitute for the repository build. The checked-in builder configuration is the canonical production build path.

# First build

The Makefile creates `venv/` automatically and installs the pinned dependencies from `requirements.txt`.

```bash
make build
```

The build target:

1. Creates/updates the Python virtual environment.
2. Runs `gftools builder` for every `sources/config*.yaml` file.
3. Recreates `fonts/`.
4. Copies distributable files into `packages/fonts/dist/fonts/`.
5. Creates the release ZIP bundle.
6. Writes `build.stamp`.

Expected generated family directories include:

```text
fonts/Obvia/
fonts/ObviaMono/
fonts/ObviaPixel/
```

Depending on family configuration they contain static TTFs, webfonts, and/or variable fonts.

## Force a clean rebuild

`build.stamp` is a Make dependency marker. If you need to force regeneration after debugging build behavior:

```bash
rm -f build.stamp
make build
```

To recreate the Python environment as well:

```bash
make clean
rm -f build.stamp
make build
```

Note that `make clean` removes the local `venv` but is not intended as a general Git cleanup command.

# Editing font sources

## Choose the correct family and style source

Do not make an upright fix in an italic source, or a Sans fix in Mono, unless the change is intentionally family-wide.

| Family | Canonical source |
| --- | --- |
| Obvia Sans upright | `sources/Obvia.glyphspackage` |
| Obvia Sans italic | `sources/Obvia-Italic.glyphspackage` |
| Obvia Mono upright | `sources/ObviaMono.glyphspackage` |
| Obvia Mono italic | `sources/ObviaMono-Italic.glyphspackage` |
| Obvia Pixel | `sources/ObviaPixel.glyphspackage` |

Every `.glyphspackage` is a directory-backed source document. Typical files include:

- `fontinfo.plist` — masters, instances, axes, custom parameters, features/classes, metrics, and family-level settings.
- `glyphs/*.glyph` — glyph layers, components, anchors, outlines, metrics, export state, and Unicode mappings.
- `order.plist` — glyph ordering used by the source.

## Glyph and Unicode changes

When adding or changing an encoded glyph:

1. Verify the Unicode code point from the Unicode Standard.
2. Use the canonical Glyphs glyph name where practical.
3. Add the glyph consistently to all styles that are expected to have equal family coverage.
4. Ensure every required master has a compatible layer.
5. Check width/sidebearings and component placement in every master.
6. Confirm that `export` is not disabled accidentally.
7. Keep `order.plist` coherent when adding a new glyph.
8. Rebuild and verify the resulting `cmap` coverage rather than assuming the source mapping exported correctly.

For related upright/italic or static/variable outputs, family codepoint coverage is expected to remain consistent unless the difference is intentional and documented.

## Outline changes

Before changing an outline:

- Check every master and brace/intermediate layer that participates in interpolation.
- Preserve contour direction and compatible point structure where interpolation requires it.
- Avoid unnecessary point-count changes.
- Remove accidental duplicate or very short segments only after visually checking the result.
- Do not automatically “fix” every QA outline warning. Some warnings are valid design choices; inspect the glyph and interpolation first.
- Recheck extrema, smooth connections, overshoots, alignment zones, and sidebearings.
- Test both the lightest and heaviest extremes as well as intermediate weights.

## Components

When changing component-based glyphs:

- Prefer components for genuinely derived forms when that remains compatible with the design.
- Verify component transforms in every master.
- Make sure automatic alignment does not move a component unexpectedly.
- Check that referenced glyphs exist in every required style.

## Anchors and combining marks

Anchor regressions often appear as shaping warnings rather than build failures.

When modifying anchors:

- Keep base and mark anchor naming consistent.
- Verify uppercase, lowercase, small/alternate, Cyrillic, Vietnamese, and localized variants that reuse the anchor system.
- Test stacked marks and dot-removal behavior for soft-dotted glyphs.
- Review italic placement separately; do not copy x positions blindly from upright sources.

## Ligatures and caret positions

Ligatures that represent multiple input characters should expose caret positions when text engines need to place a cursor inside the ligature.

For a two-character ligature, define `caret_1` in every master/layer at the intended character boundary. More complex ligatures may require additional caret anchors (`caret_2`, and so on).

Rebuild and run QA after changing ligature components or their advance widths.

## Kerning

For kerning changes:

- Prefer class kerning where glyphs share the same spacing behavior.
- Add exceptions only when the shape genuinely requires one.
- Check every master.
- Review both sides of a pair and related punctuation combinations.
- Test generated fonts; source-editor preview alone is not sufficient.

Do not “normalize” kerning by large scripted rewrites in an unrelated PR.

## OpenType features

Feature/class definitions live in the source package and may be generated automatically by Glyphs.

When changing features:

- Keep feature behavior consistent between upright and italic sources where expected.
- Verify feature compilation during `make build`.
- Test default shaping and explicitly enabled stylistic/discretionary features.
- Pay special attention to `locl`, mark/mkmk positioning, ligatures, stylistic sets, and language-specific forms.

## Metrics

Metrics changes can affect many composite glyphs and all generated instances.

Check:

- advance width and sidebearings;
- ascender/descender and vertical metrics;
- cap height/x-height relationships;
- monospaced invariants in Obvia Mono;
- math and symbol width consistency where the design expects it;
- clipping at family extremes.

Obvia Mono must remain monospaced in generated binaries. Do not judge that only from source component widths.

## Variable fonts

For variable-family edits:

- Verify the axis mapping and master locations in `fontinfo.plist`.
- Check interpolation compatibility across the full axis.
- Inspect intermediate locations, not only named instances.
- Confirm that static instances and variable outputs agree on naming, coverage, and metrics.
- Treat a variable-font-only warning separately from a static-font warning; the root cause can differ.

# Build configuration

The production builder configuration is under `sources/config-*.yaml`.

Avoid changing builder defaults merely to silence a QA warning. A configuration change can alter every binary in a family.

When changing configuration:

1. Explain why the source cannot or should not carry the fix itself.
2. Rebuild all affected outputs.
3. Compare filenames, names, axes, tables, and generated package contents before and after.
4. Include the behavioral impact in the PR description.

# QA and testing

## Fontspector

Build first, then run:

```bash
make test
```

Reports are written under:

```text
output/fontspector/
output/badges/
```

A QA warning is not automatically a design bug, and a passing build is not automatically a good font. Classify findings before fixing them:

- **Build/schema error** — fix before merging.
- **Family inconsistency** — normally fix unless intentionally documented.
- **Shaping/anchor error** — reproduce with the relevant script/language and fix at source.
- **Naming/metadata error** — verify OpenType naming and distribution requirements.
- **Outline heuristic warning** — inspect visually; do not blindly mutate contours.
- **Network/repository-service error** — distinguish infrastructure failure from a font defect.

When fixing a QA issue, note the check identifier in the commit or PR when useful.

## Proofs

Generate proofing documents with:

```bash
make proof
```

Use proofs to inspect interpolation, spacing, glyph coverage, diacritics, and text rhythm. Do not rely only on automated checks.

## Manual binary inspection

For important changes, inspect generated fonts with `fontTools`:

```bash
source venv/bin/activate
fonttools ttLib.woff2 --help >/dev/null 2>&1 || true
python - <<'PY'
from fontTools.ttLib import TTFont
font = TTFont("fonts/Obvia/ttf/Obvia-Regular.ttf")
print(font.keys())
print(font["head"].unitsPerEm)
PY
```

For codepoint coverage:

```bash
source venv/bin/activate
python - <<'PY'
from fontTools.ttLib import TTFont
font = TTFont("fonts/Obvia/ttf/Obvia-Regular.ttf")
codepoints = set()
for table in font["cmap"].tables:
    if table.isUnicode():
        codepoints.update(table.cmap)
print(f"Unicode codepoints: {len(codepoints)}")
PY
```

For a family-coverage fix, compare every generated style, not just Regular.

# npm package work

The unified package is under `packages/fonts`.

Node version:

```bash
cat .nvmrc
```

Enable Corepack and install the pinned pnpm version:

```bash
corepack enable
cd packages/fonts
pnpm install --frozen-lockfile
```

Font binaries copied into `packages/fonts/dist/fonts` are generated by `make build`. Do not manually maintain a second divergent set of font files.

If a user-facing package change requires a Changesets entry, add one in the package workflow expected by the repository maintainers. Do not bump package versions manually unless the release process explicitly requires it.

# Reviewing your diff

Before committing:

```bash
git status --short
git diff --stat
git diff
```

Check specifically for:

- repository-wide CRLF/LF churn;
- generated files unrelated to your source change;
- accidental source-editor metadata changes;
- unrelated kerning, glyph-order, or custom-parameter rewrites;
- temporary files;
- local virtual environments;
- proof output that is not intentionally part of the change.

For a source edit, it is often useful to review only the canonical sources first:

```bash
git diff -- sources/
```

# Commit conventions

Keep commits focused and use scoped Conventional Commits:

```text
fix(fonts): restore mono codepoint coverage
fix(shaping): add ligature caret positions
docs(contributing): document cross-platform build workflow
chore(build): align local QA tooling with CI
```

Do not use vague commit messages such as `fix`, `updates`, or `changes`.

If your development environment is configured for signed commits, verify the signature before pushing:

```bash
git log --show-signature -1
```

# Pull request checklist

Before opening a PR, confirm all applicable items:

- [ ] The branch contains only changes related to the stated purpose.
- [ ] Canonical edits were made under `sources/`, not directly in generated binaries.
- [ ] `make build` succeeds.
- [ ] `make test` was run and new failures are explained.
- [ ] `make proof` was reviewed for design-affecting changes.
- [ ] Upright/italic and static/variable coverage was checked where applicable.
- [ ] Interpolation was reviewed for outline/master changes.
- [ ] Kerning and anchors were checked for spacing/shaping changes.
- [ ] Obvia Mono remains monospaced when Mono sources change.
- [ ] Generated filenames and OpenType naming remain intentional.
- [ ] There is no unrelated line-ending churn.
- [ ] The PR explains any QA warning intentionally left unresolved.
- [ ] The PR includes before/after screenshots or proof excerpts when a visual design decision changed.

# What should not be automated blindly

Some font QA findings are heuristics. Do **not** apply broad automatic fixes to these without visual and interpolation review:

- short segments;
- nearly horizontal/vertical segments;
- collinear vectors;
- alignment misses;
- point simplification;
- extrema insertion;
- global width normalization;
- automatic kerning rewrites;
- anchor relocation across an entire script.

A smaller, explainable source fix is preferred over a large rewrite that happens to reduce the warning count.

# Troubleshooting

## `make build` keeps using an old result

Remove the stamp and rebuild:

```bash
rm -f build.stamp
make build
```

## Python dependency problems

Recreate the environment:

```bash
make clean
rm -f build.stamp
make build
```

## `fontspector: command not found`

Install Rust/Cargo and then:

```bash
cargo install fontspector
```

Confirm:

```bash
fontspector --version
```

## Cairo-related installation error

Install the native Cairo and `pkg-config` development packages for your operating system, then recreate the virtual environment.

On Ubuntu/WSL:

```bash
sudo apt install libcairo2-dev python3-cairo-dev pkg-config python3-dev
```

On macOS:

```bash
brew install cairo pkg-config
```

## Build works on macOS/Linux but not native Windows

Use WSL2. The repository Makefile is POSIX-oriented and is not currently a native PowerShell build script.

## Thousands of files become modified immediately after checkout

Check line endings before doing anything else:

```bash
git diff --ignore-space-at-eol --stat
```

Do not include repository-wide line-ending churn in your PR.

# Security and licensing

All contributions must be compatible with the repository's SIL Open Font License (`OFL.txt`) and project licensing requirements. Do not copy glyph outlines, kerning data, or other protected design material from fonts whose license is incompatible with this repository.

Do not commit private signing keys, tokens, credentials, local environment files, or release secrets.

# Need help?

When opening an issue or PR for a font-specific problem, include:

- family and style;
- source glyph name and Unicode code point when applicable;
- whether the problem affects static fonts, variable fonts, or both;
- operating system and application where it reproduces;
- shaping language/script and feature settings when relevant;
- a screenshot or minimal text sample for rendering problems;
- the relevant Fontspector check identifier when the issue came from QA.

That information makes font bugs significantly easier to reproduce and review.
