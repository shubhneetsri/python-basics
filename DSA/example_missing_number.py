"""
Missing Number Problems
"""

from functools import reduce

class find_missing_number():

    def __init__(self, values):
        self.values = values
    
    def getOneMissingNumber(self):
        arr = self.values
        total_expected_length = len(arr) + 1
        expected_sum = total_expected_length * (total_expected_length + 1) // 2
        actual_sum = reduce(lambda x, y: x + y, arr)
        return expected_sum - actual_sum

    def getTwoMissingNumbers(self,n):
        arr = self.values
        expected_set = set(range(1, n))
        actual_set = set(arr)
        return sorted(list(expected_set - actual_set))




# Example usage:
numbers = [1, 2, 4, 5, 6]
obj = find_missing_number(numbers)

print("One Missing number is: ", obj.getOneMissingNumber())

numbers = [1, 2, 5, 6]
obj = find_missing_number(numbers)
print("Two Missing numbers are: ", obj.getTwoMissingNumbers(6))