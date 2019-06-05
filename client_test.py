# coding=utf-8
import unittest
from unittest.mock import patch, Mock
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import firestore
import scraping
import client

class TestClient(unittest.TestCase):
    def _list_to_dict(self, _list):
        _dic = {}
        for k,v in _list:
            _dic[k] = v
        return _dic
    
    @patch.object(scraping, "get_famous_peoples")
    @patch.object(scraping, "get_famous_peoples")
    @patch.object(scraping, "get_famous_peoples")
    def get_peoples(self, mock_get_famous_people):
        mock_get_famous_people.return_value = [('Zidane','Joueur de football')]
        db = {}
        db.collection = lambda x : db
        db.document = lambda x : db
        client.get_peoples(db)
        mock_get.assert_called_with(

    def get_texts(self, db):
        for k,v in scraping.get_famous_peoples_text(scraping.get_famous_peoples()):
            db.collection('texts').document(k).set({'text':v})