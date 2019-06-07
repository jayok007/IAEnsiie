import unittest
from unittest.mock import patch, Mock, MagicMock, call
from FirestoreClient import FirestoreClient

class TestFirestoreClient(unittest.TestCase):

    def test_set_peoples(self):
        db = Mock()
        db.configure_mock(**{
            'collection.return_value': db,
            'document.return_value': db
        })
        firestore_client = FirestoreClient(db)

        firestore_client.set_peoples([
            ('Paul', 'Beautiful summary of paul'),
            ('Bob', 'Beautiful summary of bob'),
            ('Marc', 'Beautiful summary of marc')
        ])

        db.set.assert_called_once_with({
            'Paul': 'Beautiful summary of paul',
            'Bob': 'Beautiful summary of bob',
            'Marc': 'Beautiful summary of marc'
        })
        db.collection.assert_called_once_with("informations")
        db.document.assert_called_once_with("peoples")

    def test_get_peoples(self):
        peoples = {
            'Paul': 'Beautiful paul',
            'Bob': 'Beautiful bob'
        }
        db = Mock()
        db.configure_mock(**{
            'collection.return_value': db,
            'document.return_value': db,
            'get.return_value': db,
            'to_dict.return_value': peoples
        })
        firestore_client = FirestoreClient(db)

        self.assertEqual(firestore_client.get_peoples(), peoples)
        db.collection.assert_called_once_with("informations")
        db.document.assert_called_once_with("peoples")

    def test_set_texts(self):
        db = Mock()
        db.configure_mock(**{
            'collection.return_value': db,
            'document.return_value': db
        })
        firestore_client = FirestoreClient(db)

        firestore_client.set_texts([
            ('Paul', 'Beautiful paul'),
            ('Bob', 'Beautiful bob')
        ])
        self.assertEqual(db.collection.mock_calls, [call("texts"), call("texts")])
        self.assertEqual(db.document.mock_calls, [call("Paul"), call("Bob")])
        self.assertEqual(db.set.mock_calls, [
            call({ 'text': 'Beautiful paul' }),
            call({ 'text': 'Beautiful bob' })
        ])

    def test_get_text_by_name(self):
        paul = { 'text': 'Beautiful paul' }
        db = Mock()
        db.configure_mock(**{
            'collection.return_value': db,
            'document.return_value': db,
            'get.return_value': db,
            'to_dict.return_value': paul
        })
        firestore_client = FirestoreClient(db)

        self.assertEqual(firestore_client.get_text_by_name("paul"), paul)
        db.collection.assert_called_once_with("texts")
        db.document.assert_called_once_with("paul")

if __name__ == "__main__":
    unittest.main()
