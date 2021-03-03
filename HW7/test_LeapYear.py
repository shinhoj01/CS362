import pytest
from LeapYear import leapyear

class TestCase:
    def test(self):
        # lists of inputs and outputs
        inp = (2000, 2004, 1900, 2003)
        otp = ["2000 is a leap year", "2004 is a leap year",
               "1900 is not a leap year", "2003 is not a leap year"]
        # Used map to apply the function to list
        res = list(map(leapyear, inp))
        assert res == otp
