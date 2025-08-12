class A:
    def __init__(self,val):
        self.name = val
    
    def getName(self):
        return super().getName()

class C:
    def __init__(self,val):
        self.name = val
    
    def getName(self):
        return f"Hey, {self.name}"

class B(A, C):
    def __init__(self, val):
        super().__init__(val+' I am Shubhneet')
    
    def getName(self):
        return "I am B"

obj = B('hi,')
print(B.mro())
print(obj.getName())