"""
Find the largest and second largest element in an array.
"""

class greter():

    def __init__(self, value):
        self.value = value

    def getSecondLargest(self):
        values = self.value

        if len(values) < 2:
            return None
            
        for i in range(len(values)):
            for j in range(len(values)-1):
                if values[j] < values[j+1]:
                    values[j], values[j+1] = values[j+1], values[j]


        return values[1]

obj = greter([10,100,2012,11,9])
res = obj.getSecondLargest()
print(res)