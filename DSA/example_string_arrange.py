"""
Given a string "ABC", generate all possible arrangements (permutations) of its characters.

Example:

Input: "ABC"
Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
"""

class StringArrangment():

    def __init__(self,value):
        self.value = value

    def getAllArrangement(self, value=None):
        if value == None:
            value = self.value
        
        result = value[0]
        print(f"initial = {result}")

        for char in value[1:]:
            new_res = []
            for perm in result:
                for i in range(len(perm)+1):
                    new_res.append(perm[:i] + char + perm[i:])
            result = new_res
        return result


obj = StringArrangment('ABC')
print(obj.getAllArrangement())

