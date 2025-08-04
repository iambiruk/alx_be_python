import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.addition(2, 3), 5)
        self.assertEqual(self.calc.addition(-1, -1), -2)
        self.assertEqual(self.calc.addition(0, 0), 0)
        self.assertEqual(self.calc.addition(-3, -2), -1)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(10, 5), 5)
        self.assertEqual(self.calc.subtraction(5, 10), -5)
        self.assertEqual(self.calc.subtraction(0, 0), 0)
        self.assertEqual(self.calc.subtraction(-3, -2), -1)
    def test_multiply(self):
        self.assertEqual(self.calc.multiplcation(3, 4), 12)
        self.assertEqual(self.calc.multiplcation(-2, 3), -6)
        self.assertEqual(self.calc.multiplcation(0, 10), 0)
        self.assertEqual(self.calc.multiplcation(-3, -5), 15)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.3333333, place=6)
if __name__ == '__main__':

    unittest.main()


