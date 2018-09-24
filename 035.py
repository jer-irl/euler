# Generating primes using sieve of eratosthenes and then brute forcing

from typing import List

primes = set(range(2, 1000000))
for i in range(2, 1000000):
    if i not in primes:
        continue
    multiplier = 2
    while multiplier * i < 1000000:
        prod = multiplier * i
        if prod in primes:
            primes.remove(prod)
        multiplier += 1

def all_rotations(n: int) -> List[int]:
    res = []
    as_string = str(n)
    for i in range(len(as_string)):
        res.append(int(as_string[i:] + as_string[:i]))
    return res

# No pruning because I'm lazy and computers are fast
circulars = []
for prime in primes:
    rotations = all_rotations(prime)
    if all(rot in primes for rot in rotations):
        circulars.append(prime)

print(len(circulars))
