import unittest
from extractor import extracte_date

class TestExtractor(unittest.TestCase):
    def test_birthdate(self):
        dates = [
            extracte_date("né le 5 août 1912 à Lyon et mort le 22 janvier 2007 dans"),
            extracte_date("né le 28 octobre 1944 dans le 14e arrondissement de Paris et mort le 19 juin 1986 à Opio"),
            extracte_date("née Maria Salomea Skłodowska (prononcé ['marja salɔˈmɛa skwɔˈdɔfska] Médaille Nobel audio) le 7 novembre 1867 à Varsovie, au sein du royaume du Congrès (actuelle Pologne), et morte le 4 juillet 1934"),
            extracte_date("né le 23 juin 1972 à Marseille"),
            extracte_date("né le 5 septembre 1638 et mort le 1er septembre 1715"),
            extracte_date("née vers 1412 à Domrémy, village du duché de Barn 1 (actuellement dans le département des Vosges en Lorraine), et morte sur le bûcher le 30 mai 1431 à Rouen"),
            extracte_date("né à une date inconnue (vraisemblablement durant l'année 742, voire 747 ou 748, peut-être le 2 avril), mort le 28 janvier 814"),
            extracte_date("né le 1er aout 2020")
        ]

        self.assertEqual(dates, [
            ("5 août 1912", "22 janvier 2007"),
            ("28 octobre 1944", "19 juin 1986"),
            ("7 novembre 1867", "4 juillet 1934"),
            ("23 juin 1972", None),
            ("5 septembre 1638", "1er septembre 1715"),
            ("vers 1412", "30 mai 1431"),
            ("à une date inconnue", "28 janvier 814"),
            ("1er aout 2020", None)
        ])

if __name__ == "__main__":
    unittest.main()
