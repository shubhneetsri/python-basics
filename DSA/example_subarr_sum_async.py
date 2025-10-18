"""
Given an array of integers nums and an integer k,
return the total number of continuous subarrays whose sum equals k.
nums = [1, 2, 3]
k = 3
The subarrays are [1, 2] and [3].
"""
import asyncio

class subarr_prob():
    def __init__(self, value):
        self.values = value
    
    def getSubArrForTotal(self, total):
        values = self.values

        output = []
        for i in range(len(values)):
            subtotal = 0
            for j in range(i,len(values)):
                subtotal = subtotal + values[j]
                if subtotal == total:
                    output.append(values[i:j+1])
        return output
    

result = subarr_prob([1,2,3]).getSubArrForTotal(3)
print(result)


