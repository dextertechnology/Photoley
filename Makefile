SETUP_FILE = setup.py
PYTHON_FILE = /usr/bin/python3.8

build:
		$(PYTHON_FILE) $(SETUP_FILE) build

install:
		$(PYTHON_FILE) $(SETUP_FILE) install

clean:
		rm -rf dist build *.egg-info
