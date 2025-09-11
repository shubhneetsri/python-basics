"""
4SUM solution
"""

class SumGroups():

    def __init__(self, value):
        self.values = value

    def getSums(self, target):
        values = sorted(self.values)
        output = []

        for i in range(len(values)):
            left = i
            right = len(values) - 1

            while left < right:
                total = values[left] + values[left+1] + values[right] + values[right - 1] 
                if total == target:
                    output.append([values[left],values[left+1],values[right],values[right - 1]])
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return output

obj = SumGroups([-2,-1,-1,1,1,2,2])
print(obj.getSums(0))