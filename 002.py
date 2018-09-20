def summer(a, b, sum):
    theNext = a + b
    if theNext > 4000000:
        return sum
    elif (theNext % 2) == 0:
        sum += theNext

    return summer(b, theNext, sum)


def main():
    print(summer(1, 2, 2))

main()
