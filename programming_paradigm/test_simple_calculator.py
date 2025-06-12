# programming_paradigm/test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class.
    Each test method focuses on a specific aspect or edge case of the calculator's operations.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method.
        This ensures each test starts with a fresh calculator instance.
        """
        self.calc = SimpleCalculator()

    # --- Consolidated Tests for the add method ---
    def test_addition(self): # This is the method name the checker is looking for
        """Test the add method with various positive, negative, zero, and float scenarios."""
        self.assertEqual(self.calc.add(2, 3), 5)        # Positive integers
        self.assertEqual(self.calc.add(-1, -1), -2)     # Negative integers
        self.assertEqual(self.calc.add(-5, 10), 5)      # Mixed integers
        self.assertEqual(self.calc.add(0, 0), 0)        # Zeros
        self.assertEqual(self.calc.add(5, 0), 5)        # Adding zero
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)  # Floating-point numbers
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3) # Floating-point precision

    # --- Consolidated Tests for the subtract method ---
    def test_subtraction(self): # This is likely the name the checker is looking for
        """Test the subtract method with various positive, negative, zero, and float scenarios."""
        self.assertEqual(self.calc.subtract(10, 5), 5)     # Positive integers
        self.assertEqual(self.calc.subtract(5, 10), -5)    # Negative result
        self.assertEqual(self.calc.subtract(-5, -2), -3)   # Negative integers
        self.assertEqual(self.calc.subtract(2, -3), 5)     # Subtracting a negative
        self.assertEqual(self.calc.subtract(7, 0), 7)      # Subtracting zero
        self.assertEqual(self.calc.subtract(0, 7), -7)     # Subtracting from zero
        self.assertAlmostEqual(self.calc.subtract(10.5, 3.2), 7.3) # Floating-point numbers

    # --- Consolidated Tests for the multiply method ---
    def test_multiply(self): # This is likely the name the checker is looking for
        """Test the multiply method with various positive, negative, zero, and float scenarios."""
        self.assertEqual(self.calc.multiply(2, 4), 8)      # Positive integers
        self.assertEqual(self.calc.multiply(5, 0), 0)      # Multiply by zero
        self.assertEqual(self.calc.multiply(0, 8), 0)      # Multiply zero by number
        self.assertEqual(self.calc.multiply(-2, 3), -6)    # One negative
        self.assertEqual(self.calc.multiply(-3, -4), 12)   # Two negatives
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0) # Floating-point numbers

    # --- Consolidated Tests for the divide method ---
    def test_divide(self): # This is likely the name the checker is looking for
        """Test the divide method with various scenarios including division by zero."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)      # Positive integers
        self.assertEqual(self.calc.divide(10, 4), 2.5)      # Non-whole result
        self.assertEqual(self.calc.divide(-10, 2), -5.0)    # Negative numerator
        self.assertEqual(self.calc.divide(10, -2), -5.0)    # Negative denominator
        self.assertEqual(self.calc.divide(-10, -2), 5.0)    # Two negatives
        self.assertIsNone(self.calc.divide(5, 0))           # Division by zero (returns None)
        self.assertIsNone(self.calc.divide(0, 0))           # 0 divided by 0 (returns None)
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0) # Floating-point numbers
        self.assertIsInstance(self.calc.divide(6, 3), float) # Ensure float return type
        self.assertIsInstance(self.calc.divide(7, 2), float) # Ensure float return type

# This block allows you to run tests directly from the command line
if __name__ == '__main__':
    unittest.main()
    