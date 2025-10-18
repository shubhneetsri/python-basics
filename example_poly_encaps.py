from abc import ABC, abstractmethod

class vehical(ABC):
    @abstractmethod
    def startEngine(self):
        pass

class airoplane(vehical):
    def startEngine(self):
        return "Start Airoplane..."
    
class car(vehical):
    def startEngine(self):
        return "Start Car..."
    
def main(vehical:vehical):
    return vehical.startEngine()

print(main(car()))
print(main(airoplane()))
