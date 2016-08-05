def isPalindrome(n):
    theStr = list(str(n))
    pal = True
    for i in range(len(theStr) // 2):
        pal &= theStr[i] == theStr[-1 - i]
    return pal


def main():
    result = 0
    for i in reversed(range(100, 999)):
        for j in reversed(range(100, 999)):
            if i * j > result and isPalindrome(i * j):
                result = i * j
    print(result)

main()
