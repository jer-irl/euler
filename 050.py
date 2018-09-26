import itertools

primes = set(range(2, 1000001))
for i in range(2, 1000000):
    if i not in primes:
        continue
    for j in itertools.count(2):
        prod = i * j
        if prod > 1000000:
            break
        if prod in primes:
            primes.remove(prod)

primes = list(sorted(primes))

longest_total = 0
longest_count = 0
for i in range(len(primes)):
    if longest_count * primes[i] > 1000000:
        break

    total = 0
    count = 0
    for prime in primes[i:]:
        total += prime
        if total > 1000000:
            break
        if prime * (longest_count - count) + total > 1000000:
            break
        count += 1
        if total in primes and count > longest_count:
            longest_count = count
            longest_total = total

print(longest_total)
