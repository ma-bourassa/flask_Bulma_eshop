VENV_NAME?=venv
BIN=${VENV_NAME}/bin/
PYTHON=${VENV_NAME}/bin/python3

.PHONY: help install test run clean

.DEFAULT: help
help:
	@echo "make install"
	@echo "       install dependencies environment, use only once"
	@echo "make test"
	@echo "       run tests"
	@echo "make run"
	@echo "       run project"
	@echo "make clean"
	@echo "       reset project"
   

install:
	sudo apt -y install python3 python3-pip
	make venv

venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	$(BIN)pip install --no-cache-dir -r requirements.txt
	touch $(BIN)activate

test:
	${PYTHON} -m pytest

run:
	${PYTHON} run.py

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
	find -iname "*.db" -delete