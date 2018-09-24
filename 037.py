import itertools

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


def is_left_truncatable(n: int) -> bool:
    leftover = str(n)
    while leftover != "":
        if int(leftover) not in primes:
            return False
        leftover = leftover[1:]

    return True


def is_right_truncatable(n: int) -> bool:
    leftover = str(n)
    while leftover != "":
        if int(leftover) not in primes:
            return False
        leftover = leftover[:-1]

    return True


two_way_truncatable = []
for i in itertools.count(10):
    if i >= 1000000:
        raise Exception("Not enough primes")
    if is_left_truncatable(i) and is_right_truncatable(i):
        two_way_truncatable.append(i)
        if len(two_way_truncatable) >= 11:
            break

print(sum(two_way_truncatable))

