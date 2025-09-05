"""
Two SUM Problem
"""

class TwoSum():

    def __init__(self, value):
        self.value = value
    
    def get_two_sum_for_target(self,target, values = None):

        if values is None:
            values = self.value
        
        output = []
        for i in range(0,len(values)):
            for j in range(i + 1,len(values)):
                if values[i] + values[j] == target:
                    output.append([values[i],values[j]])
        return output



# def all_two_sum(nums, target):
#     results = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 results.append([i, j])
#     return results

# Example:
nums = [2, 7, 11, 15, 7]
target = 9
obj = TwoSum(nums)
print(obj.get_two_sum_for_target(target))  # Output: [[0, 1], [0, 4]]