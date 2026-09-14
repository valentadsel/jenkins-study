import unittest
from app import add


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
