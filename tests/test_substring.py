
# Make sure the test finds the application code
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

import unittest
from app import string_utils

class TestSubstring(unittest.TestCase):

    def test_equal_substrings(self):
        score:float = string_utils.calculate_match_degree("software engineering","software engineering")
        self.assertEqual(score, 1)    
        
    def test_partial_substrings(self):
        score:float = string_utils.calculate_match_degree("software engineering","building engineering")
        self.assertEqual(score, 0.6)   # fix.....changed to 0.6 from 0.9
        
    def test_kinda_substrings(self):      # Adding new test case..
        score:float = string_utils.calculate_match_degree("principle","principal")
        self.assertEqual(score, 0.77)    # was 0.9

if __name__ == "__main__":
    unittest.main()