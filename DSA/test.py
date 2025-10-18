"""
Given two strings s and t, 
write a function to determine if t is an anagram of s.
s = "listen"
t = "silent"
"""


# def get_non_repeating_char(f='open_tickets.csv'):

#     char_count = {}
#     chunk_size = 1024 * 1024

#     with open(f) as file:
#         while True:
#             chunk = file.read(chunk_size)
#             if not chunk:  # end of file
#                 break
#             for ch in chunk:
#                 if ch in char_count:
#                     char_count[ch] += 1
#                 else:
#                     char_count[ch] = 1
            
#     return char_count

# print(get_non_repeating_char())