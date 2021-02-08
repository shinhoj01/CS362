import unittest
import volume

class TestCase(unittest.TestCase):
    def test_isInteger(self):
        self.assertEqual(volume.volume(3), 27)



if __name__ == "__main__":
    unittest.main(verbosity=2)