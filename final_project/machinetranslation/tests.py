import unittest
from translator import english_to_french
from translator import french_to_english
class TestF2E(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        # Test Hello returns Bonjour
        self.assertEqual(english_to_french('hello'), 'bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(english_to_french('hello'), 'hello')
class Test(unittest.TestCase):
    """English to French tests"""
    def test2(self):
        # Test bonjour returns hello
        self.assertEqual(french_to_english('bonjour'), 'hello')
        # Test bonjour does not return bonjour
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')

if __name__ == '__main__'
unittest.main()                