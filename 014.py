bucket = {}

# Returns the length of the chain
def collatz(n):
    val = n
    i = 1
    while val != 1:
        if val in bucket:
            i += bucket[val] - 1
            break
        else:
            # even
            if val % 2 == 0:
                val = val / 2
            # odd
            elif val % 2 != 0:
                val = 3 * val + 1

            i += 1

    bucket[n] = i
    return i

def main():
    for n in range(1, 1000001):
        collatz(n)

    maxlen = max(bucket.values())

    for key in bucket:
        if bucket[key] == maxlen:
            print(key)
            return


main()
