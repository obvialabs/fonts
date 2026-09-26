PYTHON_VERSION ?= 3.11
UV ?= uv
UV_RUN = $(UV) run --no-project --python $(PYTHON_VERSION) --with-requirements requirements.txt
VERSION ?=

.PHONY: help setup build check check-full test package version proof clean

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

setup:
	$(UV) python install $(PYTHON_VERSION)
	$(UV_RUN) python -c "import fontTools, gftools; print('Python font toolchain ready')"

build:
	$(UV_RUN) python scripts/build.py

check: build
	$(UV_RUN) python scripts/check.py

check-full: build
	$(UV_RUN) python scripts/check.py --full

test: check-full

package: check-full
	$(UV_RUN) python scripts/package.py

version:
	@test -n "$(VERSION)" || (echo "VERSION is required, e.g. make version VERSION=1.4.0" && exit 1)
	$(UV_RUN) python scripts/version.py "$(VERSION)"

proof: build
	mkdir -p output/proof
	$(UV_RUN) diffenator2 proof fonts/Obvia/variable/*.ttf -o output/proof

clean:
	rm -rf output/.build-work output/release output/npm output/proof packages/fonts/dist/fonts
