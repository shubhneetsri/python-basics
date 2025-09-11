"""
Given two arrays, arr[] and dep[], 
that represent the arrival and departure times of trains respectively, 
find the minimum number of platforms required so that no train waits.
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
"""

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

platform = 0
for i in range(len(arr)):
    if i > 0:
        if arr[i] < dep[i-1]:
            platform += 1

print(platform)


