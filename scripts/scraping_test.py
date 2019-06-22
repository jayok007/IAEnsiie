# coding=utf-8
import unittest
from unittest.mock import patch, Mock
import scraping

URL = "https://fr.wikipedia.org/wiki/Le_Plus_Grand_Français_de_tous_les_temps"


class TestScraping(unittest.TestCase):

    @patch("requests.get")
    def test_get_famous_people(self, mock_get):
        mockresponse = Mock()
        mockresponse.text = """<div class="colonnes">
            <ol>
                <li><a>Test 1</a></li>
                <li><a>Test 2</a></li>
                <li><a>Test 3</a></li>
            </ol>
        </div>"""
        mock_get.return_value = mockresponse

        self.assertEqual(
            scraping.get_famous_peoples(),
            ["Test 1", "Test 2", "Test 3"]
        )
        mock_get.assert_called_with(URL)

    @patch("wikipedia.summary", return_value="Beautiful summary of Paul")
    def test_get_famous_people_text(self, mock_summary):
        text = scraping.get_famous_people_text("Paul")
        self.assertEqual(text, ("Paul", "Beautiful summary of Paul"))
        mock_summary.assert_called_with("Paul")

    # don't work on Windows :/
    @patch("wikipedia.summary", return_value="Beautiful summary")
    def test_get_famous_peoples_text(self, _):
        peoples = ["Paul", "Bob", "John"]

        self.assertEqual(scraping.get_famous_peoples_text(peoples), [
            ("Paul", "Beautiful summary"),
            ("Bob", "Beautiful summary"),
            ("John", "Beautiful summary")
        ])


if __name__ == "__main__":
    unittest.main()
