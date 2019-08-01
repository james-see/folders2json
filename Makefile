#!/bin/bash
all: clean release

release:
	@rm -rf dist build
	@python3 setup.py sdist bdist_wheel
	@echo "Build finished."
	@echo "uploading to pypi..."
	@twine upload dist/* --verbose


clean:
	@rm -rf dist build
	@rm -rf *.egg-info
	@echo "*****^^^***** fresh & clean *****^^^*****"

test:
	pytest