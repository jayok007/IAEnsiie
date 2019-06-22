install:
	pip3 install -r requirements.txt

test:
	TAGDIR=tree-tagger/ python3 -m unittest discover -s scripts -p '*_test.py'

populate:
	TAGDIR=tree-tagger/ scripts/populate_db.py
