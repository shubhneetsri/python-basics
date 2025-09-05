"""
Palindrome Example
"""

class Palindrome():
    def __init__(self, values):
        self.values = values
    
    def check_palindrome(self):
        
        value = self.values
        newstring = "" 
        
        for s in value:
            newstring = s + newstring

        if newstring == value:
            return "String is palindrome."
        else:
            print(newstring)
            return "String is not palindrome."



test_str = input("Enter the string to check palindrome: ")
new_arr = ""
obj = Palindrome(test_str)
print(obj.check_palindrome())
# print(test_str[::-1])

# arr = [s for s in list(test_str) if s!= ' ']
#
# for i in range(len(arr)):
#     loc = (len(arr)-1) - i
#     new_arr.append(arr[loc])
# new_arr = ''.join(new_arr)

# for n in test_str:
#     print(f"{n} + {new_arr}""\n")
#     new_arr = n + new_arr

# for char in test_str:
#     new_arr = char + new_arr

# if (new_arr == test_str):
#     print("String is palindrome.")
# else:
#     print("String is not palindrome.")
