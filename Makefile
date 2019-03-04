TEST_CMD = python3 -m unittest -v
CHECKSTYLE_CMD = pycodestyle --first --max-line-length=120

all: compile test checkstyle

init:
	pip install -r requirements.txt

compile:
	@echo "Nothing to compile for Python"

test:
	$(TEST_CMD) tests/test*.py

checkstyle:
	$(CHECKSTYLE_CMD) *.py snake/*.py tests/*.py

clean:
	rm -f *.pyc snake/*.pyc tests/*.pyc
	rm -rf __pycache__ snake/__pycache__ tests/__pycache__
