# coding=utf-8
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud import firestore, exceptions
import scraping


class MyFirestoreClient():
    def __init__(self):
        credentials.ApplicationDefault()
        self.db = firestore.Client()

    def _list_to_dict(self, _list):
        _dic = {}
        for k,v in _list:
            _dic[k] = v
        return _dic

    def set_peoples(self):
        try:
            self.db.collection('informations').document('peoples').set(_list_to_dict(scraping.get_famous_peoples()))
        except exceptions.NotFound:
            print('Collection not found !')

    def get_peoples(self):
        return self.db.collection('informations').document('peoples').get().to_dict()

    def set_texts(self):
        for k,v in scraping.get_famous_peoples_text(scraping.get_famous_peoples()):
            return self.db.collection('texts').document(k).set({'text':v})

    def get_text_by_name(self, name):
        try:
            return self.db.collection('texts').document(name).get().to_dict()
        except exceptions.NotFound:
            print('Collection not found !')

    # def get_texts(self):
    #     try:
    #         return db.collection('texts').to_dict()
    #     except exceptions.NotFound:
    #         print('Collection not found !')
        

if __name__ == "__main__":
    firestore_client = MyFirestoreClient()
    print(firestore_client.get_peoples())