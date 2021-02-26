import unittest
import fibonacci

class TestCase(unittest.TestCase):
    def test_fibonnaci(self):
        self.assertEqual(fibonacci.fibonacci(2), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
