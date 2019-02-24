TEST_CMD = python3 -m unittest -v
CHECKSTYLE_CMD = pycodestyle --first --max-line-length=120

all: compile test checkstyle

compile:
	@echo "Nothing to compile for Python"

test:
	$(TEST_CMD) *.py

checkstyle:
	$(CHECKSTYLE_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__
