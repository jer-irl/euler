# Not doing this in a smart way
result = 0
for i in range(1, 1001):
    tmp = 1
    for _ in range(1, i + 1):
        tmp *= i
    result += tmp

print(str(result)[-10:])
