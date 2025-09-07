"""
Given a set, generate all possible subsets (including the empty set).
Input: [1, 2, 3]
Output: [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]
"""

class Set():

    def __init__(self, setvalues):
        self.setvalues = setvalues
    
    def getAllSubSets(self, values=None, possible_sets = [[]]):
        if values == None:
            values = self.setvalues
        
        for i in values:
            subsets = []
            for j in possible_sets:
                subset = j + [i]
                subsets.append(subset)
            possible_sets.extend(subsets)

        return possible_sets

obj = Set([1, 2, 3])
print(obj.getAllSubSets())