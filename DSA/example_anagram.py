"""
Given two strings s and t, 
write a function to determine if t is an anagram of s.
s = "listen"
t = "silent"
"""

class Anagram():
    def __init__(self, values):
        self.values = values

    def isAnagram(self,val):
        value = self.values

        is_anagram = 1
        existing_char = {}
        for st in value:
            if st in val:
                existing_char[st] = existing_char.get(st, 0) + 1

        existing_char_val = {}
        for ch in val:
            existing_char_val[ch] = existing_char_val.get(ch, 0) + 1

        if existing_char == existing_char_val:
            return True
        else:
            return False

obj = Anagram("listen")
print(obj.isAnagram("silent"))