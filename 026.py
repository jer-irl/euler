# d < 1000

def largest_digit(d):
    if d // 100 != 0:
        return d // 100
    else:
        return largest_digit(d * 10)

assert(largest_digit(30) == 3)
assert(largest_digit(234) == 2)
assert(largest_digit(5) == 5)

# Basically long division
def d_to_decimal(d):
    ans = []
    val = 1
    for i in range(30):
        new_dig = val // d
        ans.append(new_dig)
        val = (val - (d * new_dig)) * 10

    # I'll Drop the first value for convenience
    ans.remove(0)
    return ans

'''
print(d_to_decimal(3))
print(d_to_decimal(5))
print(d_to_decimal(7))
'''

'''
When will they repeat? When val = 1 again
'''

# Similar to long division
def repeat_len(d):
    ans = []
    val = 1
    vals = []
    for i in range(100):
        new_dig = val // d
        ans.append(new_dig)
        val = (val - (d * new_dig)) * 10

        # End conditions
        if val == 0 and i != 0:
            #print("Terminates")
            return i
        elif new_dig == 0 and i != 0:
            #print("Terminates")
            return 0
        elif val in vals:
            print("Result")
            print(d, i)
            return i
        elif val == 1:
            return i

        vals.append(val)

'''
print(repeat_len(2))
print(repeat_len(7))
'''

result = 0
max_len = 0
for i in range(1, 1000):
    curr_len = repeat_len(i)
    if curr_len > max_len:
        max_len = curr_len
        result = i

print(result, max_len)

# Cannot get above d = 10, problem with repeat_len

