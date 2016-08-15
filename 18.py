input = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

input = input.split("\n")
input = [row.split(" ") for row in input]
input = [[int(val) for val in row] for row in input]
totRows = len(input)
print(input)

# construct a dictionary for largest path from val by index (row, col)
# 0 indexed

thedict = {}


def maxPath(index):
    result = input[index[0]][index[1]]
    # return early in last row
    if index[0] == totRows-1:
        return result

    chitlins = children(index)

    l = thedict[(chitlins[0][0], chitlins[0][1])]
    r = thedict[(chitlins[1][0], chitlins[1][1])]

    result += max([l, r])

    return result


def children(index):
    # returns list of indexes
    if index[0] == totRows - 1:
        return []
    else:
        nextRow = index[0] + 1
        return [(nextRow, index[1]), (nextRow, index[1] + 1)]


def compute():
    for rev_i, row in enumerate(reversed(input)):
        for j, val in enumerate(row):
            i = totRows - 1 - rev_i
            index = (i, j)
            thedict[index] = maxPath(index)


compute()
print(thedict[(0, 0)])
