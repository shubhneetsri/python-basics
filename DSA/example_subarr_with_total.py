"""
Given an array of positive integers
write a fn to find the smallest contiguous subarray
whose sum is greter than or equal to a target value.
"""

class SubArrayOfSum():
    def __init__(self, values):
        self.values = values
    
    def getSubArraysOfTargetSum(self, target):
        values = self.values

        output = []
        for  i in range(len(values)):
            total = 0
            for j in range(i, len(values)):
                total += values[j]
                if total == target:
                    output.append(values[i:j+1])
        return output
    
obj = SubArrayOfSum([1,5,3,6,3,6,2,1,8])
print(obj.getSubArraysOfTargetSum(9))
      