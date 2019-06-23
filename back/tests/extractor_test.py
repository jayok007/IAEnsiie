import unittest
from scripts.extractor import extract_job, extract_sexe
from scripts.extractor import extract_birthdate, extract_death

dates = [
    "né le 5 août 1912 et mort le 22 janvier 2007",
    "né le 28 octobre 1944 mort le 19 juin 1986 à Opio",
    "née ia le 7 novembre 1867 morte le 4 juillet 1934",
    "né le 23 juin 1972 à Marseille",
    "né le 5 septembre 1638 mort le 1er septembre 1715",
    "née vers 1412 morte aa aa le 30 mai 1431 à Rouen",
    "né à une date inconnue mort le 28 janvier 814",
    "né le 1er aout 2020"
]


class TestExtractor(unittest.TestCase):
    def test_birthdate(self):
        self.assertEqual(list(map(extract_birthdate, dates)), [
            "5 août 1912",
            "28 octobre 1944",
            "7 novembre 1867",
            "23 juin 1972",
            "5 septembre 1638",
            "vers 1412",
            "à une date inconnue",
            "1er aout 2020"
        ])

    def test_death_date(self):
        self.assertEqual(list(map(extract_death, dates)), [
            "22 janvier 2007",
            "19 juin 1986",
            "4 juillet 1934",
            None,
            "1er septembre 1715",
            "30 mai 1431",
            "28 janvier 814",
            None
        ])

    def test_job(self):
        jobs = [
            extract_job("est un militaire, résistant, homme d'État et écrivain français"),
            extract_job("Lino Ventura est un acteur italien, né le 14 juillet 1919"),
            extract_job("mort le 2 avril 1974 à Paris, est un haut fonctionnaire et homme d'État français."),
            extract_job("Victor est un poète, dramaturge, prosateur, romancier et dessinateur romantique français, né le 26 février"),
            extract_job("Émile Zola est un écrivain et journaliste français, né le 2 avril 1840 à Paris, où il est mort le 29 septembre 1902"),
            extract_job("Jean Gabin, à l'état civil Jean Gabin Alexis Moncorgé1, est un acteur français, né le 17 mai 1904 à Paris (9e arr.) et mort le 15 novembre 1976 à Neuilly-sur-Seine."),
            extract_job("Jacques-Yves Cousteau, né le 11 juin 1910 à Saint-André-de-Cubzac (Gironde) et mort le 25 juin 1997 à Paris, est un officier de la Marine nationale et explorateur océanographique français.")
        ]

        self.assertEqual(jobs,
            [['militaire', 'résistant', "homme d'État", 'écrivain français'],
            ['acteur italien'],
            ['haut fonctionnaire', "homme d'État français"],
            ['poète',
            'dramaturge',
            'prosateur',
            'romancier',
            'dessinateur romantique français'],
            ['écrivain', 'journaliste français'],
            ['acteur français'],
            ['officier de Marine nationale', 'explorateur océanographique français']]
        )

    def test_sexe(self):
        sexes = [
            extract_sexe("Charles de Gaulle [ ʃaʁl də ɡol]b Écouter, communément appelé le général de Gaulle ou parfois simplement le Général, né le 22 novembre 1890 à Lille et mort le 9 novembre 1970 à Colombey-les-Deux-Églises, est un militaire, résistant, homme d'État et écrivain français"),
            extract_sexe("Marie Skłodowska-Curie, ou simplement Marie Curie, née Maria Salomea Skłodowska (prononcé [ˈmarja salɔˈmɛa skwɔˈdɔfska] Médaille Nobel audio) le 7 novembre 1867 à Varsovie, au sein du royaume du Congrès (actuelle Pologne), et morte le 4 juillet 1934 au sanatorium de Sancellemoz situé à Passy (Haute-Savoie, France), est une physicienne et chimiste polonaise, naturalisée française. "),
            extract_sexe("Sœur Emmanuelle, née Madeleine Cinquin le 16 novembre 1908 à Bruxelles (Belgique) et morte le 20 octobre 2008 à Callian (Var, France), souvent surnommée la « petite sœur des chiffonniers » ou « petite sœur des pauvres », est une enseignante, religieuse et écrivain franco-belge, naturalisée égyptienne à partir de 1991."),
            extract_sexe("Yves Montand, nom de scène d'Ivo Livi, né le 13 octobre 1921 à Monsummano Terme (Italie) et mort le 9 novembre 1991 à Senlis (France), est un chanteur et acteur français d'origine italienne, naturalisé en 1929."),
        ]

        self.assertEqual(sexes, ['M', 'F', 'F', 'M'])


if __name__ == "__main__":
    unittest.main()
