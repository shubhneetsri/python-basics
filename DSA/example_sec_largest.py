"""
Get Second Largest
Fastest Way
"""

class Larger():
    def __init__(self, value):
        self.value = value
    
    def getSecondLargest(self):
        values = self.value

        if values[0] > values[1]:
            firstLarger = values[0]
            secondLarger = values[1]
        else:
            firstLarger = values[1]
            secondLarger = values[0]

        print(firstLarger)
        print(secondLarger)
        print("------------------------------")

        for i in range(2, len(values)):
            if firstLarger < values[i]:
                secondLarger = firstLarger
                firstLarger = values[i]
                        
                print(firstLarger)
                print(secondLarger)
                print("------------------------------")
            elif secondLarger < values[i]:
                secondLarger = values[i]
        return [firstLarger, secondLarger]


obj = Larger([1,9,10,3,12,99,3,55,78,91])

print(obj.getSecondLargest())