from collections import Counter

class PrimesGenerator(object):
    def __init__(self):
        self.primes = [2]
        
    def generate_up_to(self, upper_limit):
        for ctr in range(self.primes[-1] + 1, upper_limit + 1):
            if not any(ctr % p == 0 for p in self.primes):
                self.primes.append(ctr)

    def is_prime(self, n):
        self.generate_up_to(n)
        return n in self.primes

primes_gen = PrimesGenerator()

class PrimeFactorsCollection(object):
    def __init__(self, base, exp):
        self.factors = Counter()
        remaining = base

        while not primes_gen.is_prime(remaining):
            for p in primes_gen.primes:
                if remaining % p == 0:
                    self.factors[p] += 1
                    remaining //= p
                    break

        self.factors[remaining] += 1

        for factor in self.factors.keys():
            self.factors[factor] *= exp

    def __str__(self):
        res = ""
        for key in sorted(self.factors.keys()):
            res += "({},{})".format(key, self.factors[key])
        return res

uniques = set()
for base in range(2, 101):
    for exp in range(2, 101):
        uniques.add(str(PrimeFactorsCollection(base, exp)))

print(len(uniques))
