file = open("p067_triangle.txt", 'r')
input = file.read()

input = input.split("\n")
input = [row for row in input if row != '']
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
