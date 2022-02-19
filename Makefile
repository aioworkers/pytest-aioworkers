TARGET = pytest_aioworkers tests


all:

test: $(TARGET)
	isort $(TARGET)
	black $(TARGET)
	mypy $(TARGET)
	flake8 $(TARGET)

pytest_aioworkers/version.py:
	echo "__version__ = '$(shell git describe --tags)'" > $@
