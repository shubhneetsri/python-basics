"""
Given an array of numbers, 
find the maximum length of a subsequence such that 
when the subsequence is sorted, the maximum difference between adjacent numbers is 1.
Example: Write a function that returns the length of the longest subsequence 
where the difference between adjacent elements is exactly 1.
arr = [4, 2, 1, 6, 5, 3, 2, 2, 3, 4, 5, 5, 6, 7, 8]
[2, 2, 2, 3, 3]
[4, 4, 5, 5, 5]
"""

class A():
    def __init__(self, values):
        self.values = values
    
    def getSubArrs(self):
        values = self.values

        if len(values) < 2:
            return values

        svalues = sorted(values)
        print(svalues)
        output = []
        subarr = [svalues[0]] 
        for i in range(1, len(svalues)):
            if svalues[i] - svalues[i-1] in [0,1]:
                subarr.append(svalues[i])
            else:
                output.append(subarr)
                subarr = [svalues[i]]
        output.append(subarr)
        return output
    
obj = A([1, 2, 2, 3, 4, 4, 6])
print(obj.getSubArrs())
