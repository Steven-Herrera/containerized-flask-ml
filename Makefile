install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=test_app.py

lint:
	hadolint Dockerfile
	sudo pylint --disable=R,C app.py

all: install lint test