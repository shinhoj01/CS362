import unittest
import fibonacci

class TestCase(unittest.TestCase):
    def test_inputTwo(self):
        self.assertEqual(fibonacci.fibonacci(2), 1)
    def test_inputTen(self):
        self.assertEqual(fibonacci.fibonacci(10), 55)

if __name__ == "__main__":
    unittest.main(verbosity=2)
