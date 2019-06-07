install:
	pip3 install -r requirements.txt

test:
	python3 -m unittest discover -p '*_test.py'

populate:
	python3 populate_db.py
