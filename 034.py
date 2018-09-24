# I'm going to brute force with 10,000,000 as the upper bound, because 7 * 9! < 9,999,999, so
# There's no way to get factorial digits to sum to numbers as large as 10 million

def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

digit_factorials = {}
for i in range(10):
    digit_factorials[i] = factorial(i)

def digit_factorials_sum(n: int) -> int:
    digits = [int(d) for d in str(n)]
    return sum(digit_factorials[digit] for digit in digits)

total = 0
for i in range(3, 10000000):
    if digit_factorials_sum(i) == i:
        total += i

print(total)
