import itertools

def has_property(n: int) -> bool:
    as_string = str(n)
    for idx, divisor in zip(range(1, 8), [2, 3, 5, 7, 11, 13, 17]):
        digits = as_string[idx : idx + 3]
        num = int(''.join(digits))
        if num % divisor != 0:
            return False
    return True

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
total = 0
for permutation in itertools.permutations(digits):
    number = int(''.join(permutation))
    if has_property(number):
        total += number

print(total)
        
