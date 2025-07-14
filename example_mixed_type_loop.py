class NumberProb:

    def __init__(self, mixed_vals):
        self.mixed_vals = mixed_vals

    def get_numbers(self, sample=None):
        if sample is None:
            sample = self.mixed_vals

        if isinstance(sample, int):
            print(sample)
        elif isinstance(sample, (list, tuple, set)):
            for item in sample:
                self.get_numbers(item)

sample = [1, 2, 3, (4, 5, 6), 7, (8, 9, 10, [11, 12, {13, 14}])]

obj = NumberProb(sample)
obj.get_numbers()