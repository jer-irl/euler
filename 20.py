def factorial(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result

val = factorial(100)

digits = list(str(val))

result = sum([int(digit) for digit in digits])
print(result)
