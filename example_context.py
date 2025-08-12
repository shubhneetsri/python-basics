"""
The “context” refers to a block of code that runs between entering and exiting something 
— like opening a file, a DB connection, or acquiring a lock.
########################
with open(file) as file: this is live example of this concept
"""

class MyContext:

    def __new__(cls):
        print("__new__")
        return super().__new__(cls) 

    def __init__(self):
        print("__init__")

    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
    
    def __del__(self):
        print("__del__")

with MyContext() as mc:
    print("Inside with block")
    raise Exception("Oops")