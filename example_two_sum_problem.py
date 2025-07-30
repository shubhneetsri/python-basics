def all_two_sum(nums, target):
    results = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                results.append([i, j])
    return results

# Example:
nums = [2, 7, 11, 15, 7]
target = 9
print(all_two_sum(nums, target))  # Output: [[0, 1], [0, 4]]