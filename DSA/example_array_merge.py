"""
Merge two sorted arrays without extra space (with debug prints) -- Pending
"""

arr1 = [1, 2, 3, 4, 10]
arr2 = [100, 9, 200]

for j in range(len(arr2)):
    i = len(arr1) - 1 - j   # pick element from end of arr1
    print(f"Comparing {arr1[i]} and {arr2[j]}")
    if arr1[i] > arr2[j]:
        print(f"Swapping {arr1[i]} ↔ {arr2[j]}")
        arr1[i], arr2[j] = arr2[j], arr1[i]

print("\nAfter swaps (unsorted):")
print("arr1:", arr1)
print("arr2:", arr2)

# sort both arrays
arr1.sort()
arr2.sort()

print("\nAfter final sort:")
print("arr1:", arr1)
print("arr2:", arr2)
