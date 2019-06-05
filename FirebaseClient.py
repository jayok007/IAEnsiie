# coding=utf-8

import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud import firestore, exceptions
import scraping

class FirestoreClient():
    def __init__(self, db):
        credentials.ApplicationDefault()
        self.db = db

    def set_peoples(self):
        try:
            peoples = dict(scraping.get_famous_peoples())
            self.db.collection('informations').document('peoples').set(peoples)
        except exceptions.NotFound:
            print('Collection not found !')

    def get_peoples(self):
        return self.db.collection('informations').document('peoples').get().to_dict()

    def set_texts(self):
        for k, v in scraping.get_famous_peoples_text(scraping.get_famous_peoples()):
            return self.db.collection('texts').document(k).set({ 'text': v })

    def get_text_by_name(self, name):
        try:
            return self.db.collection('texts').document(name).get().to_dict()
        except exceptions.NotFound:
            print('Collection not found !')


if __name__ == "__main__":
    firestore_client = FirestoreClient(firestore.Client())
    people = firestore_client.get_text_by_name("Zinédine Zidane")
    print(people)
