install:
	pip3 install -r requirements.txt

test:
	TAGDIR=tree-tagger/ python3 -m unittest discover -s tests -p '*_test.py'

populate:
	GOOGLE_APPLICATION_CREDENTIALS=$$PWD/cred.json \
	TAGDIR=tree-tagger \
	scripts/populate_db.py

run.dev:
	GOOGLE_APPLICATION_CREDENTIALS=$$PWD/cred.json \
	FLASK_ENV=development \
	FLASK_APP=flaskr/app.py \
	flask run

.PHONY: clean
clean:
	rm -rf __pycache__ **/__pycache__
