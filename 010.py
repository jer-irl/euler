# adapted from 7

import math


def isPrime(n, primes):
    for x in primes:
        if x > math.ceil(math.sqrt(n)):
            return True
        if n % x == 0:
            return False
    return True

primes = [2, 3, 5, 7]
while primes[-1] < 2000000:
    foundPrime = False
    guess = primes[-1] + 1
    while not isPrime(guess, primes):
        guess += 1
    print(guess)
    primes.append(guess)


print(primes[:10])
print(sum(primes) - primes[-1])
