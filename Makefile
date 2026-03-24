# SOURCES: runs the parse-config.py script with the --sources flag.
# It captures the list of source files defined in the configuration
# and stores them in the SOURCES variable.
SOURCES=$(shell python3 scripts/parse-config.py --sources )

# FAMILY: runs the parse-config.py script with the --family flag.
# It extracts the familyName from the configuration file
# and stores it in the FAMILY variable.
FAMILY=$(shell python3 scripts/parse-config.py --family )

# Help target: prints available build targets and their descriptions
# It shows the user-friendly usage guide for the Makefile commands.
help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontspector"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images in the docs/ directory"
	@echo

# The 'build' target depends on 'build.stamp'.
# This means 'build.stamp' must be up to date before 'build' runs.
build: build.stamp

# The 'venv' target depends on 'venv/touchfile'.
# This is usually used to ensure a Python virtual environment exists.
venv: venv/touchfile

# The 'customize' target depends on 'venv'.
# It activates the virtual environment and runs the customize.py script.
customize: venv
	. venv/bin/activate; python3 scripts/update-license.py

# Build target: generates fonts and release artifacts
# It removes old build outputs, runs gftools builder for each config file,
# then prepares npm fonts and release zip, finally marking build completion.
build.stamp: venv sources/config-Obvia.yaml $(SOURCES)
	rm -rf fonts obvia-font obvia-font.zip
	(for config in sources/config*.yaml; do . venv/bin/activate; gftools builder $$config; done)
	$(MAKE) copy-npm-fonts
	$(MAKE) create-release-zip
	touch build.stamp

# Copy npm fonts target: prepares font files for npm distribution
# It clears old build artifacts, copies TTF/WOFF2/variable fonts into the correct package folders,
# and renames certain files to match npm naming conventions.
copy-npm-fonts:
	# Clear any pre-existing build artifacts
	rm -rf packages/next/dist/fonts
	# Copy over the relevant font files
	mkdir -p packages/fonts/dist/fonts/obvia-sans packages/fonts/dist/fonts/obvia-mono packages/fonts/dist/fonts/obvia-pixel
	cp fonts/Obvia/ttf/*.ttf packages/fonts/dist/fonts/obvia-sans/
	cp fonts/Obvia/webfonts/*.woff2 packages/fonts/dist/fonts/obvia-sans/
	cp fonts/Obvia/variable/*.ttf packages/fonts/dist/fonts/obvia-sans/
	cp fonts/ObviaMono/ttf/*.ttf packages/fonts/dist/fonts/obvia-mono/
	cp fonts/ObviaMono/webfonts/*.woff2 packages/fonts/dist/fonts/obvia-mono/
	cp fonts/ObviaMono/variable/*.ttf packages/fonts/dist/fonts/obvia-mono/
	cp fonts/ObviaPixel/webfonts/*.woff2 packages/fonts/dist/fonts/obvia-pixel/
	# Apparently there is a naming mismatch between the font files for npm distribution and the actual font files,
	# so we need to rename them to the correct names.
	cd packages/fonts/dist/fonts/obvia-sans && \
		mv Obvia-ExtraLight.ttf Obvia-UltraLight.ttf && \
		mv Obvia-ExtraLight.woff2 Obvia-UltraLight.woff2 && \
		mv Obvia-ExtraBold.ttf Obvia-UltraBlack.ttf && \
		mv Obvia-ExtraBold.woff2 Obvia-UltraBlack.woff2 && \
		mv 'Obvia[wght].ttf' Obvia-Variable.ttf && \
		mv 'Obvia[wght].woff2' Obvia-Variable.woff2
	cd packages/fonts/dist/fonts/obvia-mono && \
		mv ObviaMono-ExtraLight.ttf ObviaMono-UltraLight.ttf && \
		mv ObviaMono-ExtraLight.woff2 ObviaMono-UltraLight.woff2 && \
		mv ObviaMono-ExtraBold.ttf ObviaMono-UltraBlack.ttf && \
		mv ObviaMono-ExtraBold.woff2 ObviaMono-UltraBlack.woff2 && \
		mv 'ObviaMono[wght].ttf' ObviaMono-Variable.ttf && \
		mv 'ObviaMono[wght].woff2' ObviaMono-Variable.woff2

# Create release zip target: packages fonts and documentation into a distributable ZIP archive
# It collects all font files, selected documentation, and license text,
# then compresses them into obvia-font.zip and cleans up temporary files.
create-release-zip:
	mkdir -p obvia-font
	cp -r fonts/* obvia-font/
	cp docs/DESCRIPTION.en_us.html obvia-font/ || true
	cp docs/article/ARTICLE.en_us.html obvia-font/ || true
	cp OFL.txt obvia-font/
	zip -r obvia-font.zip obvia-font
	rm -rf obvia-font

# venv/touchfile target: sets up the Python virtual environment and installs dependencies
# It ensures the venv directory exists, installs packages from requirements.txt,
# and creates a touchfile marker to indicate the environment is ready.
venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

# Test target: runs fontspector QA checks on all font families (Obvia, ObviaMono, ObviaPixel)
# It ensures fontspector is installed, then generates HTML, Markdown, and badge reports
# for each font set. Warnings are echoed if QA checks fail.
test: build.stamp
	which fontspector || (echo "fontspector not found. Please install it with 'cargo install fontspector'." && exit 1)
	TOCHECK=$$(find fonts/Obvia/variable -type f 2>/dev/null); mkdir -p output/ output/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html output/fontspector/ObviaVF-fontspector-report.html --ghmarkdown output/fontspector/ObviaVF-fontspector-report.md --badges output/badges $$TOCHECK  || echo '::warning file=sources/config-Obvia.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/Obvia/ttf -type f 2>/dev/null); mkdir -p output/ output/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html output/fontspector/Obvia-fontspector-report.html --ghmarkdown output/fontspector/Obvia-fontspector-report.md --badges output/badges $$TOCHECK  || echo '::warning file=sources/config-Obvia.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/ObviaMono/variable -type f 2>/dev/null); mkdir -p output/ output/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html output/fontspector/ObviaMonoVF-fontspector-report.html --ghmarkdown output/fontspector/ObviaMonoVF-fontspector-report.md --badges output/badges $$TOCHECK  || echo '::warning file=sources/config-ObviaMono.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/ObviaMono/ttf -type f 2>/dev/null); mkdir -p output/ output/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html output/fontspector/ObviaMono-fontspector-report.html --ghmarkdown output/fontspector/ObviaMono-fontspector-report.md --badges output/badges $$TOCHECK  || echo '::warning file=sources/config-ObviaMono.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'
	TOCHECK=$$(find fonts/ObviaPixel/ttf -type f 2>/dev/null); mkdir -p output/ output/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html output/fontspector/ObviaPixel-fontspector-report.html --ghmarkdown output/fontspector/ObviaPixel-fontspector-report.md --badges output/badges $$TOCHECK  || echo '::warning file=sources/config-ObviaPixel.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'

# Proof target: generates proofing output using diffenator2
# It checks for variable fonts first (fonts/Obvia/variable),
# falls back to TTF fonts (fonts/Obvia/ttf) if none are found,
# then runs diffenator2 to produce proof reports in output/proof.
proof: venv build.stamp
	TOCHECK=$$(find fonts/Obvia/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/Obvia/ttf -type f 2>/dev/null); fi ; . venv/bin/activate; mkdir -p output/ output/proof; diffenator2 proof $$TOCHECK -o output/proof

# Images target: generates PNG images from Python scripts using the virtual environment
images: venv $(DRAWBOT_OUTPUT)

# Rule for converting .py files into .png images
# $< refers to the first prerequisite (the .py file)
# $@ refers to the target (the .png file)
%.png: %.py build.stamp
	. venv/bin/activate; python3 $< --output $@

# Clean target: removes the virtual environment and deletes all .pyc files
clean:
	rm -rf venv
	find . -name "*.pyc" -delete

# Update project template target: syncs with Google Fonts project template
update-project-template:
    npx update-template https://github.com/googlefonts/googlefonts-project-template/

# Update target: upgrades pip-tools, regenerates requirements.txt,
# syncs environment, and commits/pushes changes
update: venv
	venv/bin/pip install --upgrade pip-tools
	# See https://pip-tools.readthedocs.io/en/latest/#a-note-on-resolvers for
	# the `--resolver` flag below.
	venv/bin/pip-compile --upgrade --verbose --resolver=backtracking requirements.in
	venv/bin/pip-sync requirements.txt

	git commit -m "Update requirements" requirements.txt
	git push
