import unittest
from unittest.mock import Mock, call
from FirestoreClient import FirestoreClient


class TestFirestoreClient(unittest.TestCase):

    def test_set_peoples(self):
        paul = {
            'name': 'Paul',
            'text': 'Beautiful summary of paul',
            'birth_date': '13 april 1990',
            'death_date': None,
            'jobs': ['driver'],
            'sexe': 'M'
        }
        bob = {
            'name': 'Bob',
            'text': 'Beautiful summary of bob',
            'birth_date': '14 march 1991',
            'death_date': None,
            'jobs': ['cook'],
            'sexe': 'M'
        }
        db = Mock()
        db.configure_mock(**{
            'collection.return_value': db,
            'document.return_value': db
        })
        firestore_client = FirestoreClient(db)

        firestore_client.set_peoples([paul, bob])

        self.assertEqual(
            db.collection.mock_calls,
            [call("peoples"), call("peoples")]
        )
        self.assertEqual(db.document.mock_calls, [call("Paul"), call("Bob")])
        self.assertEqual(db.set.mock_calls, [call(paul), call(bob)])


if __name__ == "__main__":
    unittest.main()
