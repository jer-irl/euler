import math
import itertools

def generate_primes(primes, target):
    ctr = primes[-1] + 1
    while primes[-1] < target:
        if not any(ctr % p == 0 for p in primes):
            primes.append(ctr)
        ctr += 1

def poly_generator(a, b):
    return lambda n: (n ** 2) + (a * n) + b

primes = [2]

max_num_primes = (0, 0, -math.inf)

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        poly = poly_generator(a, b)
        number_line = itertools.count()
        for n in number_line:
            value = poly(n)
            generate_primes(primes, value)
            if value not in primes:
                if n > max_num_primes[2]:
                    max_num_primes = a, b, n
                break

print(max_num_primes)
a, b, n = max_num_primes
print(a * b)

