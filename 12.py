import math
# Need Dynamic programming


def triangle(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


def divisors(n):
    result = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return result


def nextTriangle(toAdd, prev):
    return toAdd + prev

# naive
n = 1
prev = 0
while len(divisors(nextTriangle(n, prev))) <= 500:
    print("For n = ", n)
    print("length divisors: ", len(divisors(triangle(n))))
    prev = nextTriangle(n, prev)
    n += 1

print(triangle(n))
print(len(divisors(76576500)))
