SOURCES=$(shell python3 scripts/read-config.py --sources )
FAMILY=$(shell python3 scripts/read-config.py --family )

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontspector"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the documentation/ directory"
	@echo

build: build.stamp

venv: venv/touchfile

customize: venv
	. venv/bin/activate; python3 scripts/customize.py

build.stamp: venv sources/config-Obvia.yaml $(SOURCES)
	rm -rf fonts obvia-font obvia-font.zip
	(for config in sources/config*.yaml; do . venv/bin/activate; gftools builder $$config; done)
	$(MAKE) copy-npm-fonts
	$(MAKE) create-release-zip
	touch build.stamp

copy-npm-fonts:
	# Clear any pre-existing build artifacts
	rm -rf packages/next/dist/fonts
	# Copy over the relevant font files
	mkdir -p packages/next/dist/fonts/obvia-sans packages/next/dist/fonts/obvia-mono packages/next/dist/fonts/obvia-pixel
	cp fonts/Obvia/ttf/*.ttf packages/next/dist/fonts/obvia-sans/
	cp fonts/Obvia/webfonts/*.woff2 packages/next/dist/fonts/obvia-sans/
	cp fonts/Obvia/variable/*.ttf packages/next/dist/fonts/obvia-sans/
	cp fonts/ObviaMono/ttf/*.ttf packages/next/dist/fonts/obvia-mono/
	cp fonts/ObviaMono/webfonts/*.woff2 packages/next/dist/fonts/obvia-mono/
	cp fonts/ObviaMono/variable/*.ttf packages/next/dist/fonts/obvia-mono/
	cp fonts/ObviaPixel/webfonts/*.woff2 packages/next/dist/fonts/obvia-pixel/
	# Apparently there is a naming mismatch between the font files for npm distribution and the actual font files,
	# so we need to rename them to the correct names.
	cd packages/next/dist/fonts/obvia-sans && \
		mv Obvia-ExtraLight.ttf Obvia-UltraLight.ttf && \
		mv Obvia-ExtraLight.woff2 Obvia-UltraLight.woff2 && \
		mv Obvia-ExtraBold.ttf Obvia-UltraBlack.ttf && \
		mv Obvia-ExtraBold.woff2 Obvia-UltraBlack.woff2 && \
		mv 'Obvia[wght].ttf' Obvia-Variable.ttf && \
		mv 'Obvia[wght].woff2' Obvia-Variable.woff2
	cd packages/next/dist/fonts/obvia-mono && \
		mv ObviaMono-ExtraLight.ttf ObviaMono-UltraLight.ttf && \
		mv ObviaMono-ExtraLight.woff2 ObviaMono-UltraLight.woff2 && \
		mv ObviaMono-ExtraBold.ttf ObviaMono-UltraBlack.ttf && \
		mv ObviaMono-ExtraBold.woff2 ObviaMono-UltraBlack.woff2 && \
		mv 'ObviaMono[wght].ttf' ObviaMono-Variable.ttf && \
		mv 'ObviaMono[wght].woff2' ObviaMono-Variable.woff2

create-release-zip:
	mkdir -p obvia-font
	cp -r fonts/* obvia-font/
	cp docs/DESCRIPTION.en_us.html obvia-font/ || true
	cp docs/article/ARTICLE.en_us.html obvia-font/ || true
	cp OFL.txt obvia-font/
	zip -r obvia-font.zip obvia-font
	rm -rf obvia-font

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

test: build.stamp
	which fontspector || (echo "fontspector not found. Please install it with 'cargo install fontspector'." && exit 1)
	TOCHECK=$$(find fonts/Obvia/variable -type f 2>/dev/null); mkdir -p output/ output/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html output/fontspector/ObviaVF-fontspector-report.html --ghmarkdown output/fontspector/ObviaVF-fontspector-report.md --badges output/badges $$TOCHECK  || echo '::warning file=sources/config-Obvia.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/Obvia/ttf -type f 2>/dev/null); mkdir -p output/ output/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html output/fontspector/Obvia-fontspector-report.html --ghmarkdown output/fontspector/Obvia-fontspector-report.md --badges output/badges $$TOCHECK  || echo '::warning file=sources/config-Obvia.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/ObviaMono/variable -type f 2>/dev/null); mkdir -p output/ output/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html output/fontspector/ObviaMonoVF-fontspector-report.html --ghmarkdown output/fontspector/ObviaMonoVF-fontspector-report.md --badges output/badges $$TOCHECK  || echo '::warning file=sources/config-ObviaMono.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/ObviaMono/ttf -type f 2>/dev/null); mkdir -p output/ output/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html output/fontspector/ObviaMono-fontspector-report.html --ghmarkdown output/fontspector/ObviaMono-fontspector-report.md --badges output/badges $$TOCHECK  || echo '::warning file=sources/config-ObviaMono.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/ObviaPixel/ttf -type f 2>/dev/null); mkdir -p output/ output/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html output/fontspector/ObviaPixel-fontspector-report.html --ghmarkdown output/fontspector/ObviaPixel-fontspector-report.md --badges output/badges $$TOCHECK  || echo '::warning file=sources/config-ObviaPixel.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'

proof: venv build.stamp
	TOCHECK=$$(find fonts/Obvia/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/Obvia/ttf -type f 2>/dev/null); fi ; . venv/bin/activate; mkdir -p output/ output/proof; diffenator2 proof $$TOCHECK -o output/proof

images: venv $(DRAWBOT_OUTPUT)

%.png: %.py build.stamp
	. venv/bin/activate; python3 $< --output $@

clean:
	rm -rf venv
	find . -name "*.pyc" -delete

update-project-template:
	npx update-template https://github.com/googlefonts/googlefonts-project-template/

update: venv
	venv/bin/pip install --upgrade pip-tools
	# See https://pip-tools.readthedocs.io/en/latest/#a-note-on-resolvers for
	# the `--resolver` flag below.
	venv/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements.in
	venv/bin/pip-sync requirements.txt

	git commit -m "Update requirements" requirements.txt
	git push
