# I'm going to do my own conversion to binary, instead of built-in python

powers_2 = [1]
while powers_2[-1] < 1000000:
    powers_2.append(powers_2[-1] * 2)

powers_2 = list(reversed(powers_2))


def to_binary(n: int) -> str:
    res = ""
    leftover = n
    for power in powers_2:
        if power > leftover:
            res += "0"
        else:
            res += "1"
            leftover -= power

    # Strip leading zeros
    res = list(res)
    res = res[res.index("1"):]
    res = "".join(res)

    return res


def is_palindrome(x: str) -> bool:
    for i, letter in enumerate(x[: len(x) // 2]):
        if letter != x[len(x) - 1 - i]:
            return False

    return True


dbl_base_palindromes = [x for x in range(1, 1000000) if is_palindrome(str(x)) and is_palindrome(to_binary(x))]

print(sum(dbl_base_palindromes))
