import itertools

def all_permutations(*lst):
    digits = [set([int(c) for c in list(str(x))]) for x in lst]
    return all(item1 == item2 for item1 in digits for item2 in digits)


primes = set(range(2, 10000))
for i in range(2, 10000):
    if i not in primes:
        continue
    for mult in itertools.count(2):
        prod = mult * i
        if prod > 10000:
            break
        if prod in primes:
            primes.remove(prod)
primes = [p for p in sorted(primes) if 1000 <= p < 10000]

for i, starting_prime in enumerate(primes):
    for second_prime in primes[i + 1:]:
        third_num = second_prime + (second_prime - starting_prime)
        if third_num not in primes:
            continue
        if all_permutations(starting_prime, second_prime, third_num):
            print(starting_prime, second_prime, third_num)


