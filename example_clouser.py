"""
Python Clouser
A function inside another function that remembers the outer function’s variables 
even after the outer function is done.
"""

def parent():
    x: int = 2

    def child():
        print(x)
    
    # returns a child function
    return child

def create_febonnici():
    x, y = 0, 1

    def febonnici():
        nonlocal x, y
        res = x
        x, y = y, x + y
        return res

    return febonnici
        

# parent_output = parent()
# parent_output() 

feb = create_febonnici()
print(feb())
print(feb())
print(feb())
print(feb())
print(feb())