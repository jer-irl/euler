import math

def factors(n):
    result = set()
    for i in range(math.ceil(math.sqrt(n))):
        j = i + 1
        if n % j == 0:
            result.add(j)
            result.add(n // j)
    return result

def proper_factors(n):
    result = factors(n)
    result.remove(n)
    return result

def get_abundants():
    result = []
    for i in range(1, 28124):
        fact_sum = sum(proper_factors(i))
        if fact_sum > i:
            result.append(i)
    return result


abundants = get_abundants()

abundant_sums = set()
for x in abundants:
    for y in abundants:
        abundant_sums.add(x + y)

result = 0
for i in range(1, 28124):
    if i not in abundant_sums:
        result += i

print(result)

