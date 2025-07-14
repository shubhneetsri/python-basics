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

parent_output = parent()
parent_output() 