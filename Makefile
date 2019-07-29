#!/bin/bash
DEBUG = 0;

all: clean release

release:
	rm -rf dist build
	if '[ -f setup.py ]'; then
		echo "File not found!"
	else
	python3 setup.py sdist bdist_wheel
	fi
	twine upload dist/* --verbose

clean:
	@rm -rf dist build
	@rm -rf *.egg-info
	@echo "fresh and clean"

test:
	pytest