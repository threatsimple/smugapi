
VENV_DIR=./pyvenv

DEFAULT=dev

$(VENV_DIR): virtualenv

rundev:
	$(VENV_DIR)/bin/smugapi run --debug -b 0.0.0.0

test:
	$(VENV_DIR)/bin/pytest

testx:
	# stop after first error
	$(VENV_DIR)/bin/pytest -x

clean:
	rm -rf $(VENV_DIR) build dist
	find . -type d -name __pycache__ | xargs rm -rf
	find . -type d -name smugapi.egg-info | xargs rm -rf

virtualenv: $(VENV_DIR)/bin/activate
$(VENV_DIR)/bin/activate:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r reqs_dev.pip

dev: virtualenv
	$(VENV_DIR)/bin/pip install -e .

bumpver:
	bin/incr_build VERSION

tagproj:
	git tag -a v`cat VERSION`
	git push --tags

pkg: virtualenv
	$(VENV_DIR)/bin/pip install --upgrade setuptools wheel
	$(VENV_DIR)/bin/python3 setup.py sdist bdist_wheel

pkg_upload: virtualenv
	$(VENV_DIR)/bin/pip install --upgrade twine
	$(VENV_DIR)/bin/twine upload dist/*

build_docker:
	docker build -t threatsimple/smugapi:`cat VERSION` .


