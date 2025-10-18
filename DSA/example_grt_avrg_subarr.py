"""
Given a list of numbers, find the greatest average of any three consecutive numbers in the list.
nums = [1, 12, 5, 6, 2, 9, 8]
Consecutive triplets: [1,12,5], [12,5,6], [5,6,2], [6,2,9], [2,9,8]

Their averages: (1+12+5)/3=6, (12+5+6)/3=7.67, (5+6+2)/3=4.33, (6+2+9)/3=5.67, (2+9+8)/3=6.33

Greatest average = 7.67
"""
class A():
    def __init__(self, values):
        self.values = values
    
    def getMaxAvrg(self):
        values = self.values

        output = {}
        for i in range(len(values)-2):

            left = i
            middle = i + 1
            right = i + 2

            avrg = (values[i] + values[middle] + values[right]) / 3
            output[round(avrg)]=[values[i],values[i+1],values[i+2]]
        return output

obj = A([1, 12, 5, 6, 2, 9, 8])
print(obj.getMaxAvrg())

