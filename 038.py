import itertools


def has_pandigital_multiple(n: int):
    prefixes = [int(str(n)[:i]) for i in range(1, len(str(n)))]
    for i in prefixes:
        if i * (10 ** len(str(i))) > n:
            return False

        concatenated_str = ""
        for multiplier in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            new_mult = i * multiplier
            concatenated_str += str(new_mult)
            if int(concatenated_str) == n:
                return True
            elif int(concatenated_str) > n:
                break
            elif str(n)[:len(concatenated_str)] != concatenated_str:
                break



digits = ['9', '8', '7', '6', '5', '4', '3', '2', '1']

for permutation in itertools.permutations(digits):
    number = int(''.join(permutation))
    if has_pandigital_multiple(number):
        print(number)
        break
