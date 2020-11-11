import unittest
from src.compare import compare

class TestCompare(unittest.TestCase):
    
# compare_test.py
    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_5_10_returns_5_is_less_than_10(self):
        self.assertEqual("5 is less than 10", compare(5, 10))

    def test_compare_5_5_returns_numbers_are_the_same(self):
        self.assertEqual("numbers are the same", compare(5, 5))