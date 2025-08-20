# Parent class
class Calculator:
    def add(self, *args, **kwargs):
        total = 0
        # Add all positional arguments
        for num in args:
            total += num
        # Add all keyword arguments values
        for key, value in kwargs.items():
            total += value
        return total

# Child class overrides add (polymorphism)
class DoubleCalculator(Calculator):
    def add(self, *args, **kwargs):
        # Double the result
        total = super().add(*args, **kwargs)
        return total * 2

# Usage
calc = Calculator()
print(calc.add(1, 2, 3, a=4, b=5))  # 15

double_calc = DoubleCalculator()
print(double_calc.add(1, 2, 3, a=4, b=5))  # 30
