from functools import reduce
import time
from functools import lru_cache

arr = [1,3,5,7,10,9]
k = len(arr)


print(arr[2::-1])




# nums = [1, 2, 3, 4, 5]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)  # ➜ [2, 4]

# sets = {1,2,3,4,5,6,7,8,9,10}
# get = set(map(lambda x: x * 3, sets))
# print(get)

# sets = {1,2,3,4,5,6,7,8,9,10}
# get = reduce(lambda x, y: x if x>y else y, sets)
# print(get)


# # A slow function simulating a time-consuming calculation
# @lru_cache(maxsize=3)  # Cache up to 3 calls
# def slow_square(n):
#     print(f"Computing square of {n}...")
#     time.sleep(2)  # Simulate delay
#     return n * n

# # Call with some numbers
# print(slow_square(3))  # Takes ~2 seconds, prints "Computing square of 3..."
# print(slow_square(4))  # Takes ~2 seconds, prints "Computing square of 4..."
# print(slow_square(3))  # Cached result, instant, no print
# print(slow_square(5))  # Takes ~2 seconds, prints "Computing square of 5..."
# print(slow_square(4))  # Cached result, instant, no print
# print(slow_square(6))  # Takes ~2 seconds, prints "Computing square of 6..."

# # Now the cache size is 3, so the oldest cache entry (3) is discarded
# print(slow_square(3))  # Not cached anymore, takes ~2 seconds, prints "Computing square of 3..."
