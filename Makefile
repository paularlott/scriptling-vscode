# Makefile for building Scriptling VSCode Extension

OUT_DIR = out
DIST_DIR = dist
VERSION = $(shell node -p "require('./package.json').version")

.PHONY: clean install compile lint build package release publish publish-release watch

clean:
	rm -rf $(OUT_DIR)
	rm -rf $(DIST_DIR)

install:
	npm install

compile:
	npm run compile

lint:
	npm run lint

build: compile

package: compile
	mkdir -p $(DIST_DIR)
	npx vsce package --out $(DIST_DIR)/scriptling-$(VERSION).vsix

release: package
	# Check if tag exists
	if git tag -l v$(VERSION) | grep -q v$(VERSION); then \
		echo "Tag v$(VERSION) already exists, skipping tag creation"; \
	else \
		echo "Creating tag v$(VERSION)"; \
		git tag -a v$(VERSION) -m "Release $(VERSION)"; \
		git push origin v$(VERSION); \
	fi
	# Create release and upload vsix
	gh release create v$(VERSION) -t "Release $(VERSION)" -n "Scriptling VSCode Extension $(VERSION)" $(DIST_DIR)/scriptling-$(VERSION).vsix

publish: package
	npx vsce publish --packagePath $(DIST_DIR)/scriptling-$(VERSION).vsix

publish-release: package
	$(MAKE) publish
	$(MAKE) release

watch:
	npm run watch
