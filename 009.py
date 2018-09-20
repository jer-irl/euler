# a**2 + b**2 = c**2
# a + b + c = 1000


def check(a, b, c):
    result = (a ** 2 + b ** 2 == c ** 2)
    return result

for i in range(1000):
    for j in range(1000):
        if i + j < 1000:
            c = 1000 - i - j
            if check(i, j, c):
                print(i*j*c)
