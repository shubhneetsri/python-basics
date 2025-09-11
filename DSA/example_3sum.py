"""
Three SUM Logical problem
"""

class SumProblem():
    def __init__(self, value):
        self.value = value

    def solve_3sum(self, target):
        values = self.value

        output = []
        for i in range(len(values)):
            for j in range(i+1,len(values)):
                for k in range(j+1,len(values)):
                    if values[i] + values[j] + values[k] == target:
                        output.append([values[i],values[j],values[k]])
        return output
    
    def solve_3sum_optimized(self, target):
        values = sorted(self.value)
        len_values = len(values)
        output = []

        for i in range(len_values - 2):
            if i > 0 and values[i] == values[i-1]:
                continue  # skip duplicate starting numbers

            left, right = i + 1, len_values - 1
            while left < right:
                total = values[i] + values[left] + values[right]
                if total == target:
                    output.append([values[i], values[left], values[right]])

                    # skip duplicates for left & right
                    # while left < right and values[left] == values[left+1]:
                    #     left += 1
                    # while left < right and values[right] == values[right-1]:
                    #     right -= 1

                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return output

obj = SumProblem([1,2,3,4,5,6,7,8,9,12,16,10,0,-1])
print(obj.solve_3sum_optimized(15))
print(obj.solve_3sum(15))

