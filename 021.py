import math

# really ugly solution

divisors = {}
for n in range(10000):
    divisors[n] = set()
divisors[2].add(1)
divisors[3].add(1)
divisors[4].add(1)
divisors[4].add(2)

def gen_divisors(n):
    cand = 1
    while (cand <= math.ceil(math.sqrt(n))):
        if n % cand == 0:
            divisors[n].add(cand)
            divisors[n].add(n // cand)
            if cand in divisors:
                divisors[n] = divisors[n] | divisors[cand]
            if n // cand in divisors:
                divisors[n] = divisors[n] | divisors[n // cand]
        cand += 1

def d(n):
    if n in divisors:
        return sum(divisors[n])
    else:
        return False

for n in range(10000):
    gen_divisors(n)

for key in divisors:
    divisors[key].discard(key)

ds = {}
for key in divisors:
    ds[key] = d(key)

amicables = []
for key in ds:
    if ds[key] != key and ds[key] in ds and ds[ds[key]] == key:
        amicables.append(key)


print(sum(amicables))
