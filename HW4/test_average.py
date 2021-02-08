import unittest
import average

class TestCase(unittest.TestCase):
    def test_isNumber(self):
        self.assertEqual(average.find_average([1,2,3]), 2)

    def test_isNumberwithFloat(self):
        self.assertEqual(average.find_average([1.2,2.2,3.2]), 2.2)

    def test_emptyList(self):
        self.assertFalse(average.find_average([]))

    def test_isString(self):
        self.assertFalse(average.find_average(["string", "Hello", "World"]))

    def test_isMixed(self):
        self.assertFalse(average.find_average(["one", 2, 3.8]))

if __name__ == "__main__":
    unittest.main(verbosity=2)