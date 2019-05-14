import unittest
from unittest.mock import patch, Mock
import requests
from scraping import get_famous_people

class TestScraping(unittest.TestCase):

    @patch.object(requests, "get")
    def test_upper(self, mock_get):
        mockresponse = Mock()
        mock_get.return_value = mockresponse
        mockresponse.text = """<div class="colonnes">
            <ol>
                <li><a href="/test_1">Test 1</a></li>
                <li><a href="/test_2">Test 2</a></li>
            </ol>
        </div>"""

        self.assertEqual(get_famous_people(), [
            ("Test 1", "https://fr.wikipedia.org/test_1"),
            ("Test 2", "https://fr.wikipedia.org/test_2")
        ])
        mock_get.assert_called_with("https://fr.wikipedia.org/wiki/Le_Plus_Grand_Français_de_tous_les_temps")

if __name__ == "__main__":
    unittest.main()
