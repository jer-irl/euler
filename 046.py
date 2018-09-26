import itertools

primes = [2]

def generate_primes_up_to(n):
    for candidate in range(primes[-1], n + 1):
        if not any(candidate % p == 0 for p in primes):
            primes.append(candidate)
    return True


def goldbach_correct(n: int) -> bool:
    generate_primes_up_to(n)
    for prime in primes:
        if prime >= n:
            break
        for i in range(1, n):
            total = prime + 2 * (i ** 2)
            if total > n:
                break
            if total == n:
                return True
    return False

odd_composite_generator = (x for x in itertools.count(3, 2) if generate_primes_up_to(x) and x not in primes)

for i in odd_composite_generator:
    if not goldbach_correct(i):
        print(i)
        break

