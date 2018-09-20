import math


def gcd(a, b):
    while b > 0:
        z = a % b
        a = b
        b = z
    return a


def isPrime(n):
    for factor in range(2, math.ceil(math.sqrt(n))):
        if n % factor == 0:
            return False
    return True


def main():
    i = 2
    while i < 600851475143:
        if 600851475143 % i == 0:
            candidate = 600851475143 // i
            if isPrime(candidate):
                print(candidate)
            if isPrime(i):
                print(i)
        i += 1
main()
