# coding=utf-8
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import firestore
import scraping

def _list_to_dict(_list):
    _dic = {}
    for k,v in _list:
        _dic[k] = v
    return _dic

def set_peoples(db):
    try:
        db.collection('informations').document('peoples').set(_list_to_dict(scraping.get_famous_peoples()))
    except google.cloud.exceptions.NotFound:
        print('Collection not found !')

def get_peoples(db):
    return db.collection('informations').document('peoples').get().to_dict()

def set_texts(db):
    for k,v in scraping.get_famous_peoples_text(scraping.get_famous_peoples()):
        return db.collection('texts').document(k).set({'text':v})

def get_texts(db, name):
    try:
        return db.collection('texts').document(name).get().to_dict()
    except google.cloud.exceptions.NotFound:
        print('Collection not found !')
        

if __name__ == "__main__":
    cred = credentials.ApplicationDefault()
    db = firestore.Client()
    print(get_peoples(db))