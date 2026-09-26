# Obvia Fonts developer entry points.
#
# The Makefile intentionally stays thin: complex build, validation, packaging,
# and release behavior lives in scripts/ so Windows/WSL, Linux, macOS, and CI
# execute the same implementation instead of duplicating shell logic.

# Python toolchain used by every repository command. uv installs/uses this
# interpreter independently from the system Python and avoids PEP 668 issues.
PYTHON_VERSION ?= 3.11
UV ?= uv
UV_RUN = $(UV) run --no-project --python $(PYTHON_VERSION) --with-requirements requirements.txt
VERSION ?=

.PHONY: help setup build check check-full test package version proof clean

# Help target: print the supported public developer commands.
help:
	@echo "Obvia Fonts"
	@echo
	@echo "  make setup        Install/verify the pinned Python toolchain with uv"
	@echo "  make build        Rebuild all fonts and release artifacts"
	@echo "  make check        Build, then validate generated binaries and package layout"
	@echo "  make check-full   Build, validate, and run blocking Fontspector QA"
	@echo "  make package      Build + full QA + create an inspectable npm tarball"
	@echo "  make version VERSION=x.y.z"
	@echo "                    Update @obvia/fonts version for a release PR"
	@echo "  make proof        Build and generate Diffenator2 proof output"
	@echo "  make clean        Remove generated local outputs"

# Setup target: ensure the pinned Python interpreter and core font tooling are
# available. No global pip installation or repository-local legacy venv is used.
setup:
	$(UV) python install $(PYTHON_VERSION)
	$(UV_RUN) python -c "import fontTools, gftools; print('Python font toolchain ready')"

# Build target: compile every source family into an isolated staging directory,
# then atomically replace generated output only after the complete build succeeds.
build:
	$(UV_RUN) python scripts/build.py

# Fast validation target: rebuild and validate manifests, OpenType binaries,
# codepoint coverage invariants, and the npm distribution layout.
check: build
	$(UV_RUN) python scripts/check.py

# Release-grade validation target: run the same checks plus blocking Fontspector
# Google Fonts profile checks. FAIL results stop CI; WARN results remain reports.
check-full: build
	$(UV_RUN) python scripts/check.py --full

# Backwards-compatible test alias retained for contributors used to `make test`.
test: check-full

# Package target: build, run full quality checks, compile the npm wrapper, inspect
# the publication allow-list, and create the exact .tgz used by staged publishing.
package: check-full
	$(UV_RUN) python scripts/package.py

# Version target: update only the package.json version value. The helper preserves
# the repository's existing hand-aligned JSON formatting and whitespace.
version:
	@test -n "$(VERSION)" || (echo "VERSION is required, e.g. make version VERSION=1.4.0" && exit 1)
	$(UV_RUN) python scripts/version.py "$(VERSION)"

# Proof target: generate visual Diffenator2 proof output from the built variable
# Obvia family. Build runs first so proofing always sees current binaries.
proof: build
	mkdir -p output/proof
	$(UV_RUN) diffenator2 proof fonts/Obvia/variable/*.ttf -o output/proof

# Clean target: remove generated/transient outputs only. Source packages and
# committed package wrapper files are intentionally never removed.
clean:
	rm -rf output/.build-work output/release output/npm output/proof packages/fonts/dist/fonts
