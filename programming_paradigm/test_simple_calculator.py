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

    # --- Tests for the add method ---
    def test_addition_positive_integers(self):
        """Test add method with two positive integers."""
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_integers(self):
        """Test add method with negative integers."""
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-5, 10), 5) # Mix of positive and negative

    def test_addition_zero(self):
        """Test add method with zero."""
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)

    def test_addition_floats(self):
        """Test add method with floating-point numbers."""
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3) # Use assertAlmostEqual for floats

    # --- Tests for the subtract method ---
    def test_subtract_positive_integers(self):
        """Test subtract method with two positive integers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5) # Result is negative

    def test_subtract_negative_integers(self):
        """Test subtract method with negative integers."""
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(2, -3), 5) # Subtracting a negative

    def test_subtract_zero(self):
        """Test subtract method with zero."""
        self.assertEqual(self.calc.subtract(7, 0), 7)
        self.assertEqual(self.calc.subtract(0, 7), -7)

    def test_subtract_floats(self):
        """Test subtract method with floating-point numbers."""
        self.assertAlmostEqual(self.calc.subtract(10.5, 3.2), 7.3)

    # --- Tests for the multiply method ---
    def test_multiply_positive_integers(self):
        """Test multiply method with positive integers."""
        self.assertEqual(self.calc.multiply(2, 4), 8)

    def test_multiply_by_zero(self):
        """Test multiply method when one operand is zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 8), 0)

    def test_multiply_negative_integers(self):
        """Test multiply method with negative integers."""
        self.assertEqual(self.calc.multiply(-2, 3), -6) # One negative
        self.assertEqual(self.calc.multiply(-3, -4), 12) # Two negatives

    def test_multiply_floats(self):
        """Test multiply method with floating-point numbers."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 2.0), 5.0)

    # --- Tests for the divide method ---
    def test_divide_positive_integers(self):
        """Test divide method with positive integers."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(10, 4), 2.5) # Non-whole result

    def test_divide_negative_integers(self):
        """Test divide method with negative integers."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

    def test_divide_by_zero(self):
        """Test divide method when the denominator is zero (should return None)."""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Test 0 / 0 case as well

    def test_divide_floats(self):
        """Test divide method with floating-point numbers."""
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_divide_result_type(self):
        """Ensure successful division always returns a float."""
        self.assertIsInstance(self.calc.divide(6, 3), float)
        self.assertIsInstance(self.calc.divide(7, 2), float)


# This block allows you to run tests directly from the command line
if __name__ == '__main__':
    unittest.main()