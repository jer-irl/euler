import itertools

def is_prime(n):
    for divisor in range(2, n // 2):
        if n % divisor == 0:
            return False
    return True

digits = list('987654321')

for i in range(len(digits)):
    digit_subset = digits[i:]
    for perm in itertools.permutations(digit_subset):
        if is_prime(int(''.join(perm))):
            print(int(''.join(perm)))
            exit(0)


