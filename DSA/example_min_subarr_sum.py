"""
Problem: Minimum Size Subarray Sum

Given an array of positive integers nums and an integer target, 
return the minimal length of a contiguous subarray of which the sum is greater than or equal to target. 
If no such subarray exists, return 0.
Input: nums = [2,3,1,2,4,3], target = 7  
Output: 2  
Explanation: The subarray [4,3] has the minimal length = 2
"""

class SubArr():
    def __init__(self, values):
        self.values = values
    
    def getMinSubArr(self, target):
        values = self.values
    
        output = []

        for i in range(len(values)):
            subarr = []
            total = 0
            start = i
            while total < target and start < len(values):
                subarr.append(values[start])
                total += values[start]
                start += 1

            if total >= target:
                output.append(list(subarr))

        return output

obj = SubArr([2,3,1,2,4,3])
print(obj.getMinSubArr(7))
