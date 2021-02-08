import unittest
import volume

class TestCase(unittest.TestCase):
    def test_isInteger(self):
        self.assertEqual(volume.find_volume(3), 27)
    
    def test_isFloat(self):
        self.assertEqual(volume.find_volume(5.8), 5.8 * 5.8 * 5.8)

    def test_isString(self):
        self.assertEqual(volume.find_volume("string"), -1)

    def test_isNegative(self):
        self.assertEqual(volume.find_volume(-4), -1)

if __name__ == "__main__":
    unittest.main(verbosity=2)