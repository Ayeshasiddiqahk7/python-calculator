import unittest  # Import the unittest module
from calculator import Calculator  # Import the Calculator class

class TestCalculator(unittest.TestCase):
    """Unit tests for the Calculator class."""

    @classmethod
    def setUpClass(cls):
        """Initialize a Calculator instance before running tests."""
        cls.calc = Calculator()  # Create a Calculator object for testing

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Check if 2 + 3 = 5

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 2), 3)  # Check if 5 - 2 = 3

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(4, 3), 12)  # Check if 4 * 3 = 12

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)  # Check if 10 / 2 = 5

    def test_divide_by_zero(self):
        """Test the divide method with division by zero."""
        with self.assertRaises(ZeroDivisionError):  # Check if ZeroDivisionError is raised
            self.calc.divide(10, 0)  # Try to divide by zero

if __name__ == '__main__':
    unittest.main()  # Run the unit tests