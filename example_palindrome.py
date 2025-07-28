"""
Palindrome Example
"""


# def run(test_str):
#     return {'result': reverse(test_str)}

test_str = input("Enter the string to check palindrome: ")
new_arr = ""
# print(test_str[::-1])

# arr = [s for s in list(test_str) if s!= ' ']
#
# for i in range(len(arr)):
#     loc = (len(arr)-1) - i
#     new_arr.append(arr[loc])
# new_arr = ''.join(new_arr)

for n in test_str:
    print(f"{n} + {new_arr}""\n")
    new_arr = n + new_arr

if (new_arr == test_str):
    print("String is palindrome.")
else:
    print("String is not palindrome.")
