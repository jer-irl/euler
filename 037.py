import itertools

primes = [2]


def generate_primes_up_to(limit):
    for candidate in range(primes[-1] + 1, limit + 1):
        if not any(candidate % p == 0 for p in primes):
            primes.append(candidate)


def is_left_truncatable(n: int) -> bool:
    generate_primes_up_to(n)
    leftover = str(n)
    while leftover != "":
        if int(leftover) not in primes:
            return False
        leftover = leftover[1:]

    return True


def is_right_truncatable(n: int) -> bool:
    generate_primes_up_to(n)
    leftover = str(n)
    while leftover != "":
        if int(leftover) not in primes:
            return False
        leftover = leftover[:-1]

    return True


two_way_truncatable = []
for i in itertools.count(10):
    if is_left_truncatable(i) and is_right_truncatable(i):
        print(i)
        two_way_truncatable.append(i)
        if len(two_way_truncatable) >= 11:
            break

print(two_way_truncatable)
print(sum(two_way_truncatable))

