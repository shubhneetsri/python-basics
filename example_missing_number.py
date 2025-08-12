from functools import reduce

def find_missing_number(arr):
    n = len(arr) + 1  # Total numbers from 1 to n
    expected_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
    actual_sum = reduce(lambda x,y: x + y, arr)
    return expected_sum - actual_sum

# Example usage:
numbers = [1, 2, 4, 5, 6]
missing = find_missing_number(numbers)
print("Missing number is:", missing)

def find_two_missing_numbers(arr, n):
    full_set = set(range(1, n + 1))
    actual_set = set(arr)
    missing = list(full_set - actual_set)
    return sorted(missing)

# Example usage:
numbers = [1, 2, 4, 6]
n = 6  # Total numbers from 1 to 6
missing_numbers = find_two_missing_numbers(numbers, n)
print("Missing numbers are:", missing_numbers)