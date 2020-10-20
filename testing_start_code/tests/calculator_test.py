
import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        expected = 6
        actual = add(2, 4)
        self.assertEqual(expected, actual)

    def test_substract(self):
        self.assertEqual(3, subtract(9,6))

    def test_divide(self):
        self.assertEqual(5, divide(10,2))

    def test_multiply(self):
        self.assertEqual(30, multiply(5,6))