import unittest
from main_helpers import *

class TestMainHelpers(unittest.TestCase):
    def test_headline_extractor(self):
        text = "# Hello"
        headline = extract_title(text)        
        self.assertEqual(headline, "Hello")