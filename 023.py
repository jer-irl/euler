import math

def factors(n):
    result = []
    for i in range(math.ceil(math.sqrt(n))):
        i += 1
        if n % i == 0:
            result.append(n)
            result.append(n // i)
    return result

def get_abundants():
    result = []
    for i in range(28124):
        fact_sum = sum(factors(i))
        if fact_sum > i:
            result.append(i)
    return result

print(len(get_abundants()))
