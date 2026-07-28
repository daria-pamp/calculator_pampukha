import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):

    def test_example_1(self):
        # (3 + 2) * 3 = 15
        instructions = [
            "add 2",
            "multiply 3",
            "apply 3"
        ]
        self.assertEqual(calculate(instructions), 15)

    def test_example_2(self):
        # 5 * 9 = 45
        instructions = [
            "multiply 9",
            "apply 5"
        ]
        self.assertEqual(calculate(instructions), 45)

    def test_whitespace_and_empty_lines(self):
        # Test resilience against extra whitespace and blank lines
        instructions = [
            "  add 2  ",
            "",
            " multiply 3 ",
            "   ",
            "apply 3"
        ]
        self.assertEqual(calculate(instructions), 15)

    def test_float_numbers(self):
        # (10.5 + 2.5) / 2 = 6.5
        instructions = [
            "add 2.5",
            "divide 2",
            "apply 10.5"
        ]
        self.assertEqual(calculate(instructions), 6.5)

    def test_division_by_zero(self):
        instructions = [
            "divide 0",
            "apply 10"
        ]
        with self.assertRaises(ZeroDivisionError):
            calculate(instructions)

    def test_missing_apply(self):
        instructions = [
            "add 5",
            "multiply 2"
        ]
        with self.assertRaises(ValueError):
            calculate(instructions)


if __name__ == '__main__':
    unittest.main()