arr = [1,2,3,4,5,6,7,8,9,10]

print(arr)

for i in range(len(arr)):
    print(arr[i])

    first = []
    second = []

    left = i
    right = len(arr) - 1
    while left < right:
        first.append(arr[left])
        second.append(arr[right])
        right -= 1
        left += 1

    # for j in range(len(arr)-1-i,-1,-1):
    #     second.append(arr[j])
    print(first)
    print(second)