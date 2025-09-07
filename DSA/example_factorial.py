"""
Factorial Problem
"""

class Factorial():

    def __init__(self, value):
        self.value = value

    def getFactorial(self, value=None):
        if value == None:
            value = self.value

        if value == 0 or value == 1:
            return value
        
        while value > 0:
            return value * self.getFactorial(value-1)     
        
obj = Factorial(5)
print(obj.getFactorial())
