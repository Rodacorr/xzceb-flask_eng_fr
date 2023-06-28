import unittest

from tests import frenchtoenglish, englishtofrench

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench("hello"), "bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchtoenglish("bonjour"), "hello")
        

class TestEnglishToFrenchNegative(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(frenchtoenglish("hello"), "Keloke")

class TestFrenchToEnglishNegative(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(frenchtoenglish("bonjour"), "Keloke")

if __name__ == "__main__":
    unittest.main()
