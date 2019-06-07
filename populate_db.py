# coding=utf-8
from firebase_admin import credentials
from google.cloud import firestore
from scraping import get_famous_peoples, get_famous_peoples_text
from FirestoreClient import FirestoreClient

if __name__ == "__main__":
    firestore_client = FirestoreClient(firestore.Client())
    peoples_text = get_famous_peoples_text(get_famous_peoples())
    firestore_client.set_texts(peoples_text)
