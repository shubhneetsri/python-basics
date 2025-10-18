from abc import ABC, abstractmethod

class flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class movable(ABC):
    @abstractmethod
    def run(self):
        pass

class execute(movable, flyable):
    def __init__(self):
        pass

    def run(self):
        return "Running..."
    
    def fly(self):
        return "Flying...."

obj = execute()
print(obj.run())
print(obj.fly())