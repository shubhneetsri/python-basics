"""
Kadane’s Algorithm: Maximum Subarray Sum
"""
class max_subarray():
    def __init__(self, values):
        self.values = values

    def getMaxSubArraysForTarget(self, target):
        values = self.values

        output = []
        final = []
        for i in range(len(values)):
            total = 0
            output = []
            for j in range(i,len(values)):
                total += values[j]
                output.append(values[j]) # we never touched final, but it changed because this output append when use plain output in line 20
                if total == target:
                    final.append(list(output)) # should append a copy of output OR use list() to make it new
                    
        return final


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj = max_subarray(arr)
print(obj.getMaxSubArraysForTarget(6))