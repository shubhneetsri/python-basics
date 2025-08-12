class MagicMethodsDemo:
    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("__init__ called")
        self.value = value

    def __str__(self):
        return f"__str__ called: Value is {self.value}"

    def __repr__(self):
        return f"MagicMethodsDemo({self.value})"

    def __len__(self):
        print("__len__ called")
        return len(str(self.value))

    def __getitem__(self, key):
        print(f"__getitem__ called with key={key}")
        return str(self.value)[key]

    def __setitem__(self, key, value):
        print(f"__setitem__ called with key={key}, value={value} (simulated)")

    def __delitem__(self, key):
        print(f"__delitem__ called with key={key} (simulated)")

    def __call__(self, *args, **kwargs):
        print(f"__call__ called with args={args}, kwargs={kwargs}")

    def __eq__(self, other):
        print("__eq__ called")
        return self.value == other.value

    def __add__(self, other):
        print("__add__ called")
        return MagicMethodsDemo(self.value + other.value)

    def __sub__(self, other):
        print("__sub__ called")
        return MagicMethodsDemo(self.value - other.value)

    def __mul__(self, other):
        print("__mul__ called")
        return MagicMethodsDemo(self.value * other.value)

    def __truediv__(self, other):
        print("__truediv__ called")
        return MagicMethodsDemo(self.value / other.value)

    def __enter__(self):
        print("__enter__ called (context manager)")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ called (context manager)")

    def __del__(self):
        print("__del__ called (destructor)")


# Test all magic methods
if __name__ == "__main__":
    # print("Creating instance...")
    a = MagicMethodsDemo(10)
    # b = MagicMethodsDemo(5)

    # print("\nString representation:")
    # print(a)
    # # print(repr(a))

    # print("\nLength:")
    # print(len(a))

    # print("\nItem access:")
    # print(a[0])
    # a[1] = "X"
    # del a[1]

    # print("\nCalling instance:")
    # a()

    # print("\nEquality check:")
    # print(a == b)

    # print("\nArithmetic operations:")
    # c = a + b
    # print(c)

    # d = a - b
    # print(d)

    # e = a * b
    # print(e)

    # f = a / b
    # print(f)

    # print("\nContext manager test:")
    # with MagicMethodsDemo(100) as obj:
    #     print("Inside with block:", obj)

    # print("\nDeleting objects...")
    # del a
    # del b
    # del c
    # del d
    # del e
    # del f

    print("\nDone.")
