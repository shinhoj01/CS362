import unittest
from leapYearHandle import checkLeap

class TestCase(unittest.TestCase):
    def test_isString(self):
        checkLeap("hello world")
    def test_isLeapBy400(self):
        checkLeap("2000")
    def test_isNotLeapBy100(self):
        checkLeap("1900")
    def test_isLeapBy4(self):
        checkLeap("2004")
    def test_isNotLeap(self):
        checkLeap("2003")
