import pytest
import code

class TestCase:
    def test(self):
        # lists of inputs and outputs
        inp = (2,3,5,9,10,15,55,75,99,100)
        otp = [2,"Fizz","Buzz","Fizz","Buzz","FizzBuzz",
               "Buzz","FizzBuzz","Fizz","Buzz"]
        # Used map to apply the function to list
        res = list(map(code, inp))
        assert res == otp
