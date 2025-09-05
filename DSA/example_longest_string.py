"""
Longest SubString Without Repeating Char
"""

class longestString():
    def __init__(self,value):
        self.value = value
    
    def getLengthOfLongestString(self, value = None):
        
        if value is None:
            value = self.value
        
        if len(value) < 1:
            return value

        stack = []
        final = []
        for val in value:
            if val not in stack:
                stack.append(val)
            else:
                break

        final.append("".join(stack))
        final.extend(self.getLengthOfLongestString(value[1:]))
        return final

obj = longestString('abcabcklmnwert')
output = obj.getLengthOfLongestString()
print(output)