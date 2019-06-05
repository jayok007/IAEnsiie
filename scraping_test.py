import unittest
from unittest.mock import patch, Mock
import requests
from scraping import get_famous_peoples, get_famous_peoples_text, get_famous_people_text

class TestScraping(unittest.TestCase):

    @patch.object(requests, "get")
    def test_get_famous_people_url(self, mock_get):
        mockresponse = Mock()
        mockresponse.text = """<div class="colonnes">
            <ol>
                <li><a href="/test_1">Test 1</a></li>
                <li><a href="/test_2">Test 2</a></li>
            </ol>
        </div>"""
        mock_get.return_value = mockresponse

        self.assertEqual(get_famous_peoples(), [
            ("Test 1", "https://fr.wikipedia.org/test_1"),
            ("Test 2", "https://fr.wikipedia.org/test_2")
        ])
        mock_get.assert_called_with("https://fr.wikipedia.org/wiki/Le_Plus_Grand_Français_de_tous_les_temps")

    @patch.object(requests, "get")
    def test_get_famous_peoples_text(self, mock_get):
        mockresponse = Mock()
        mockresponse.text = """<div id="bodyContent">
            <p>Hello</p>
            <p>Hi</p>
            <p>Good morning</p>
        </div>"""
        mock_get.return_value = mockresponse

        peoples = [
            ("Paul", "http://example.com/test_1"),
            ("Bob", "http://example.com/test_2"),
            ("John", "http://example.com/test_3")
        ]

        self.assertEqual(get_famous_peoples_text(peoples), [
            ("Paul", "\nHello\nHi\nGood morning\n"),
            ("Bob", "\nHello\nHi\nGood morning\n"),
            ("John", "\nHello\nHi\nGood morning\n")
        ])

    @patch.object(requests, "get")
    def test_get_famous_people_text(self, mock_get):
        mockresponse = Mock()
        mockresponse.text = """<div id="bodyContent">
            <p>Hello</p>
            <p>Hi</p>
            <p>Good morning</p>
        </div>"""
        mock_get.return_value = mockresponse

        result = get_famous_people_text(("Paul", "http://example.com/test_1"))

        self.assertEqual(result, ("Paul", "\nHello\nHi\nGood morning\n"))

if __name__ == "__main__":
    unittest.main()
