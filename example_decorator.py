"""
Decorator
"""

class UnauthorizedError(Exception):
    pass

class Payment():

    def __init__(self, user_type):
        self.user_type = user_type

    @staticmethod
    def auth(fn):
        def child(self, *args, **kwargs):
            if self.user_type == 'admin':
                return fn(self, *args, **kwargs)
            else:
                raise UnauthorizedError("Access Denied")
        return child
    
    @auth
    def iamfn(self, value):
        print(value)



# obj = Payment('admin')
# obj.iamfn('Hey, i am here')

obj = Payment('guest')
try:
    obj.iamfn("Hey, i am here")
except UnauthorizedError as e:
    print(e)  # Output: Access Denied