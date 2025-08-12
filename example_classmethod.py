class A():
    def __init__(self,val):
        self.name = val

    @classmethod
    def myname(cls, val):
        if val < 10:
            val += 1
            return cls(val)
        else:
            return val

    def getName(self):
        return self.name
        
class B(A):
    def __init__(self, val):
        super().__init__('B Calling...')
        print(self.name)
        print(self.myname(val))

B(1)
