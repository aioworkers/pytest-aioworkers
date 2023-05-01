FILES = $(wildcard pytest_aioworkers/*.py)
FILES += $(wildcard tests/*.py)

TARGET = pytest_aioworkers tests


all:

.coverage: $(FILES)
	hatch run cov
	hatch run cov:cov

.PHONY: cov
cov: .coverage
	hatch run coverage report

htmlcov/index.html: .coverage
	hatch run coverage html
