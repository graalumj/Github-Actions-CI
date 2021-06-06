import unittest
import calculator


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(1, 1), 0)

    def test_mutliply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)

if __name__ == '__main__':
    unittest.main()
