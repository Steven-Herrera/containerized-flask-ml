install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=test_app.py

lint:
	hadolint Dockerfile
	pylint --disable=R,C venv/app.py

all: install lint test