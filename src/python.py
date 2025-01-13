# Dictionary
customers = {
    'name' : 'Teka',
    'age' : 21,
    "city" : 'Atlanta'
}

for k, v in customers.items():
    #print(f"{k}: {v}")
    pass

# Exceptions
try:
    print(1/0)

except Exception as ex:
    #print(ex)
    pass
# Classes
class MyClass:
    my_number = 123456

    def fun(self):
        print("My function inside a class.")
        return "Everything good!"
    
# print(MyClass().fun())

# print(sum(x for x in range(101)))

# Standard Library
import os
# print(os.getcwd())
import glob
# print(glob.glob('*.py'))
from datetime import date
#print(date.today())

def average(values):
    """Computes the arithmetic mean of a list of numbers.

     print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)
list = [2, 4, 7]
average(list)
import doctest
doctest.testmod()   # automatically validate the embedded tests


import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 5.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests