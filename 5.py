def check(n):
    result = True
    for i in range(20):
        result &= (n % (i + 1)) == 0
    return result


def main():
    theDivs = [x + 1 for x in range(20)]
    cand = 1
    for x in theDivs:
        cand *= x

    for div in reversed(theDivs):
        if check(cand / div):
            cand /= div
    print(cand)

main()
