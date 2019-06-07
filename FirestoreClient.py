# coding=utf-8
from firebase_admin import credentials
from google.cloud import firestore, exceptions

class FirestoreClient():
    def __init__(self, db):
        credentials.ApplicationDefault()
        self.db = db

    def set_peoples(self, peoples):
        try:
            self.db.collection('informations').document('peoples').set(dict(peoples))
        except exceptions.NotFound:
            print('Collection not found !')

    def get_peoples(self):
        return self.db.collection('informations').document('peoples').get().to_dict()

    def set_texts(self, peoples_text):
        for name, text in peoples_text:
            self.db.collection('texts').document(name).set({ 'text': text })

    def get_text_by_name(self, name):
        try:
            return self.db.collection('texts').document(name).get().to_dict()
        except exceptions.NotFound:
            print('Collection not found !')
