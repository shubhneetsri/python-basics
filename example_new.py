class testnew:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("__new__ Creating instance")
            cls._instance = super().__new__(cls)
        else:
            print("__new__ Returning existing instance")
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            print("Now call __init__")
            self.__class__._initialized = True


# Test
a = testnew()
b = testnew()