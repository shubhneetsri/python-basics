def create_multipliers():
    return [lambda x: i * x for i in range(5)]

multipliers = create_multipliers()
print([m(2) for m in multipliers])  # What is the output?