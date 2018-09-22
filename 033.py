import functools

fractions = []

for denominator in range(10, 100):
    denom_digits = [int(d) for d in str(denominator)]
    for numerator in range(10, denominator):
        # Trivial examples
        if denominator % 10 == 0 and numerator % 10 == 0:
            continue

        num_digits = [int(d) for d in str(numerator)]

        shared_digits = {x for x in num_digits if x in denom_digits}
        if len(shared_digits) == 0:
            continue

        for shared_digit in shared_digits:
            reduced_num = num_digits.copy()
            reduced_num.remove(shared_digit)
            reduced_num = reduced_num[0]
            reduced_denom = denom_digits.copy()
            reduced_denom.remove(shared_digit)
            reduced_denom = reduced_denom[0]

            if reduced_denom == 0:
                continue

            if numerator / denominator == reduced_num / reduced_denom:
                fractions.append((reduced_num, reduced_denom))

nums, denoms = zip(*fractions)
num = functools.reduce(lambda acc, x: acc * x, nums, 1)
denom = functools.reduce(lambda acc, x: acc * x, denoms, 1)

primes = [2]
def generate_primes_up_to(x):
    for candidate in range(primes[-1] + 1, x + 1):
        if not any(candidate % p == 0 for p in primes):
            primes.append(candidate)

def prime_factors(n):
    generate_primes_up_to(n)

    factors = []
    leftover = n
    while leftover not in primes:
        for prime in primes:
            if leftover % prime == 0:
                factors.append(prime)
                leftover /= prime
    return factors

num_factors = prime_factors(num)
denom_factors = prime_factors(denom)

while any(x in denom_factors for x in num_factors):
    shared = [x for x in num_factors if x in denom_factors]
    num_factors.remove(shared[0])
    denom_factors.remove(shared[0])

reduced_num = functools.reduce(lambda acc, x: acc * x, num_factors, 1)
reduced_denom = functools.reduce(lambda acc, x: acc * x, denom_factors, 1)
print(reduced_denom)
