"""
Given two arrays, arr[] and dep[], 
that represent the arrival and departure times of trains respectively, 
find the minimum number of platforms required so that no train waits.
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
"""

class platform():

    def __init__(self, arr, dep):
        self.arr = arr
        self.dep = dep

    def find_required_platforms(self):
        
        arr = self.arr
        dep = self.dep

        platforms = 0
        for i in range(len(arr)):
            if i > 0:
                if arr[i] < dep[i-1]:
                    platforms += 1

        return platforms


# arr.sort()
# dep.sort()
# platform_needed = 0

# for i in range(len(arr)):
#     count = 1
#     for j in range(len(dep)):
#         if arr[i] < dep[j]:
#             count += 1

# print(count)


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
obj = platform(arr,dep) 
output = obj.find_required_platforms()
print(output)