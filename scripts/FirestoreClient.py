# coding=utf-8


class FirestoreClient():
    def __init__(self, db):
        self.db = db

    def set_peoples(self, peoples):
        for people in peoples:
            infos = self.db.collection('peoples')
            infos.document(people['name']).set(people)

    def get_peoples(self):
        collection = self.db.collection('peoples').get()
        return [c.to_dict() for c in collection]
