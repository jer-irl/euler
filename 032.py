import itertools

def is_pandigital(a, b, prod, digits):
    input_digits = [int(char) for char in str(a) + str(b) + str(prod)]
    return (len(input_digits) == len(digits) and
            all(d in input_digits for d in digits))

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pandigital_prods = set()

for a_len in range(1, 10):
    for a_digits in itertools.permutations(digits, a_len):
        leftover_for_b = [d for d in digits if d not in a_digits]
        a = int(''.join(str(d) for d in a_digits))

        # Must be at least one leftover for product
        for b_len in range(1, len(leftover_for_b)):
            for b_digits in itertools.permutations(leftover_for_b, b_len):
                b = int(''.join(str(d) for d in b_digits))
                prod = a * b

                if is_pandigital(a, b, prod, digits):
                    pandigital_prods.add(prod)

print(sum(pandigital_prods))
