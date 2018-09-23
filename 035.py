primes = [2]
def generate_primes_up_to(x):
    for candidate in range(primes[-1] + 1, x + 1):
        if not any(candidate % p == 0 for p in primes):
            primes.append(candidate)

generate_primes_up_to(1000000)
print(primes)
