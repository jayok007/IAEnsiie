# coding=utf-8


class FirestoreClient():
    def __init__(self, db):
        self.db = db

    def set_peoples(self, peoples):
        for people in peoples:
            infos = self.db.collection('peoples')
            infos.document(people['name']).set(people)
