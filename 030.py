# I'm going to brute force with 1000000 as the upper bound, because 7 * 9^5 < 1000000, so no
# numbers greater than 1000000 can be summed to by the sum of their digits raised to the fifth
# power

def digit_fifth_powers_sum(n: int):
    digits = [int(digit) for digit in str(n)]
    return sum(digit ** 5 for digit in digits)

total = 0
for i in range(2, 1000000):
    if digit_fifth_powers_sum(i) == i:
        total += i

print(total)
