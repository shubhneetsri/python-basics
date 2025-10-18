class B():
    def __init__(self):
        self.name='kenya'

    def getname(self):
        return self.name

class D(B):
    def __init__(self, name, email):
        super(D,self).__init__()
        self.email = email
    
    def getname(self):
        return self.name
    
print(D('Test','ssss').getname())