"""
Reverse a string without using slicing
"""

import asyncio

class reverse():
    def __init__(self, value):
        self.value = value
    
    async def getRevString(self,sleepttime):
        await asyncio.sleep(sleepttime)
        return await self.getReverse()

    async def getReverse(self):
        value = self.value

        reversed = ''
        for val in range(len(value)-1,-1,-1):
            reversed = reversed + value[val]
        return reversed

async def main():
    obj1 = reverse('abcd')
    obj2 = reverse('opopopopopopo')
    obj3 = reverse('aaaaaaaaaaaaaaasdgfgfg')

    task = [
        obj1.getRevString(7),
        obj2.getRevString(1),
        obj3.getRevString(2)
    ]

    for t in asyncio.as_completed(task):
        print(await t)

    # result = await asyncio.gather(
    #     obj1.getRevString(7),
    #     obj2.getRevString(1),
    #     obj3.getRevString(2)
    # )
    
    # for output in result:
    #     print(output)

asyncio.run(main())