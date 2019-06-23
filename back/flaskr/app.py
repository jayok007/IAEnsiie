from flask import Flask, jsonify
from google.cloud import firestore
from firebase_admin import credentials
from scripts.FirestoreClient import FirestoreClient
from random import randrange

app = Flask(__name__)
credentials.ApplicationDefault()
firestore_client = FirestoreClient(firestore.Client())


@app.route('/peoples')
def get_peoples():
    peoples = firestore_client.get_peoples()
    return jsonify(peoples)


@app.route('/random-people')
def random_people():
    peoples = firestore_client.get_peoples()
    n = randrange(0, len(peoples))
    return jsonify(peoples[n])
