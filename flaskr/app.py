from flask import Flask, jsonify
from google.cloud import firestore
from firebase_admin import credentials
from scripts.FirestoreClient import FirestoreClient

app = Flask(__name__)
credentials.ApplicationDefault()
firestore_client = FirestoreClient(firestore.Client())


@app.route('/peoples')
def hello():
    peoples = firestore_client.get_peoples()
    return jsonify(peoples)
