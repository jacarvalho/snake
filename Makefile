TEST_CMD = python3 -m unittest -v
CHECKSTYLE_CMD = pycodestyle --first --max-line-length=120

all: compile test checkstyle

init:
	pip install -r requirements.txt

compile:
	@echo "Nothing to compile for Python"

test:
	$(TEST_CMD) tests/test_*.py

checkstyle:
	$(CHECKSTYLE_CMD) *.py snake/*.py tests/*.py

clean:
	rm -f *.pyc
	rm -rf __pycache__
