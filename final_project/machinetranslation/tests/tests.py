import unittest

from translator import englishtofrench, frenchtoenglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(englishtofrench("test"), "")
        self.assertEqual(englishtofrench("Hello"), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(frenchtoenglish("test"), "")
        self.assertEqual(frenchtoenglish("Bonjour"), "Hello")

unittest.main()