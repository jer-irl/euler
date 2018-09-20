import math


primes = [2]
while len(primes) < 10001:
    print(len(primes))
    foundPrime = False
    guess = primes[-1] + 1
    while not foundPrime:
        guessRoot = math.ceil(math.sqrt(guess))
        for x in primes:
            if guess % x == 0 or x > guessRoot:
                guess += 1
                continue
        foundPrime = True
    primes.append(guess)

print(primes[-1])
