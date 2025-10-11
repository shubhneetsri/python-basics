"""
Group words by anagrams → e.g., ["eat","tea","tan","ate","nat","bat"] → [['eat','tea','ate'], ['tan','nat'], ['bat']].
"""

import asyncio

class anagram():
    def __init__(self, input_value):
        self.value = input_value
    
    def getExactGroups(self):
        values = self.value

        anagram_groups = {}
        for val in values:
            key = ''.join(sorted(val))
            
            if key in anagram_groups:
                anagram_groups[key].append(val)
            else:
                anagram_groups[key] = [val]
        return anagram_groups


    # Tried but not peract
    def getGroups(self):
        values = self.value

        final_groups = []
        for i in range(len(values)):
            group_segment = [values[i]]
            for j in range(i+1,len(values)):
                if len(values[i]) == len(values[j]):
                    isTrue = True
                    for latter in values[i]:
                        if latter not in values[j]:
                            isTrue = False
                            break
                    if isTrue == True:
                        group_segment.append(values[j])
            final_groups.append([group_segment])
        return final_groups

obj = anagram(["eat","tea","tan","ate","nat","bat"])
result = obj.getExactGroups()
print(result)