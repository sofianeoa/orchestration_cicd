import unittest
from calcules import Calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Calculator.addition(2, 3), 5)

    def test_multiplication(self):
        self.assertEqual(Calculator.multiplication(3, 2), 6)

    def test_division(self):
        self.assertEqual(Calculator.division(4, 2), 2)
        with self.assertRaises(ZeroDivisionError):
            Calculator.division(1, 0)

    def test_subtraction(self):
        self.assertEqual(Calculator.subtraction(5, 1), 4)

if __name__ == '__main__':
    unittest.main()
