"""
Sort the array
"""

def merge_sort(list):

    if len(list) <= 1:
        return list
    
    mid = len(list) // 2
    LList = merge_sort(list[:mid])
    RList = merge_sort(list[mid:])

    i = j = 0
    sort_list = []

    while i < len(LList) and j < len(RList):
        if LList[i] < RList[j]:
            sort_list.append(LList[i])
            i += 1
        else:
            sort_list.append(RList[j])
            j += 1

    sort_list.extend(LList[i:])
    sort_list.extend(RList[j:])
    return sort_list

def bubble_sort(list_arr):
    l = len(list_arr)
    for i in range(l):
        for j in range(l - i -1):
            if list_arr[j] > list_arr[j+1]:
                temp = list_arr[j+1]
                list_arr[j+1] = list_arr[j]
                list_arr[j] = temp
    return list_arr

sorted_list = bubble_sort([2,1,5,4,6,9,1,0])
print(sorted_list)