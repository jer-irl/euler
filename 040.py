# Just coding the pattern, and then going along it

class PatternIterator:
    def __init__(self):
        self.counter = 1
        self.digits_from_counter = "1"

    def __iter__(self):
        return self

    def __next__(self):
        if self.digits_from_counter == "":
            self.counter += 1
            self.digits_from_counter = str(self.counter)
        res = int(self.digits_from_counter[0])
        self.digits_from_counter = self.digits_from_counter[1:]
        return res

idxs_to_mult_at = [1, 10, 100, 1000, 10000, 100000, 1000000]
prod = 1
for i, digit in enumerate(PatternIterator()):
    if i == idxs_to_mult_at[-1]:
        break
    if i + 1 in idxs_to_mult_at:
        prod *= digit
print(prod)

