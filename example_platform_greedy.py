"""
Given two arrays, arr[] and dep[], 
that represent the arrival and departure times of trains respectively, 
find the minimum number of platforms required so that no train waits.
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
"""
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

arr.sort()
dep.sort()
platform_needed = 0

for i in range(len(arr)):
    count = 1
    for j in range(len(dep)):
        if arr[i] < dep[j]:
            count += 1

print(count)