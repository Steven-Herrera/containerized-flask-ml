setup:
	python3 -m venv ~/.containerized-flask-app && source ~/.containerized-flask-app/bin/activate
	
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
format:
	black *.py
	
lint:
	pylint --disable=R,C app.py
	
test:
	python -m pytest -vv test_app.py
	
all: install lint test