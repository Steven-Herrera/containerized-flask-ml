install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_app.py
	
docker-lint:
	hadolint Dockerfile

lint:
	pylint --disable=R,C app.py

all: install lint test