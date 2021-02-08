import unittest
import namegen

class TestCase(unittest.TestCase):
    def test_rightCase(self):
        self.assertEqual(namegen.generate("Hojun", "Shin"), "Hojun Shin")

    def test_containSpaceF(self):
        self.assertFalse(namegen.generate("Ho jun", "Shin"))

    def test_containSpecF(self):
        self.assertFalse(namegen.generate("#8$un", "Shin"))

    def test_containSpaceL(self):
        self.assertFalse(namegen.generate("Hojun", "S  n"))

    def test_containSpecL(self):
        self.assertFalse(namegen.generate("Hojun", "$4in"))

    def test_containSpaceBoth(self):
        self.assertFalse(namegen.generate("Ho jun", "  in"))

    def test_containSpecBoth(self):
        self.assertFalse(namegen.generate("3o#@$", "Sh0$"))

if __name__ == "__main__":
    unittest.main(verbosity=2)