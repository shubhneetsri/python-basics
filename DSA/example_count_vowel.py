"""
Count vowels and consonants in a string.
"""
import asyncio

class AlphaFilter():

    def __init__(self, value):
        self.value = value
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    async def getFilter(self):
        value_to_filter = self.value
        vowels = self.vowels

        vowel_found = []
        constant_found = []
        for val in value_to_filter:
            if val in vowels:
                vowel_found.append(val)
            else:
                constant_found.append(val)
        return {'vowels':vowel_found, 'constants':constant_found}


async def main():
    results = await asyncio.gather(
        AlphaFilter('AIoddf;jfgjdvfskjdhgkjhdfgjsdfhkgjhdfkgjhdksfjghdfkjghkdfjghurytuierytiuerytiuerytiuerytiuyrtiurytiureytiurtyiurtyiuretyiuertyiuretyiufdhgadlssdflasdfdjbvncbvxcbvmzx,xbxcnv').getFilter(),
        AlphaFilter('ABCD').getFilter(),
        AlphaFilter('jdfsgksdfuretiuuyfdfgasjdfhgajshdgfkahgsdfkahsdgfkahsdgfkjahsdsgfkjhdgfjhasdgf').getFilter()
    )
    return results

# Run all coroutines concurrently
result = asyncio.run(main())
print(result)