BIN=venv/bin/

.PHONY: help prepare-dev test run

.DEFAULT: help
help:
	@echo "make install"
	@echo "       prepare development environment, use only once"
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
	$(BIN)pip install -r requirements.txt

test: venv
	${BIN}python -m pytest

run: venv
	${BIN}python app.py

clean:
	rm -rf venv
	find -iname "*.pyc" -delete



