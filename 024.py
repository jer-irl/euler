# I won't use fancy python tools, but instead do this manually.  itertools would
# make it trivial, as there are only 3000000 permutations

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def permutations(head, tail):
    if tail == []:
        yield head
    else:
        for num in tail:
            new_head = head + [num]
            new_tail = tail.copy()
            new_tail.remove(num)
            yield from permutations(new_head, new_tail)

perm_generator = permutations([], nums)

for i in range(1000000):
    res = next(perm_generator)

print("".join([str(x) for x in res]))
