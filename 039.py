# Just brute forcing

def is_right_triangle(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


sols = {}
for p in range(1, 1001):
    sols[p] = []
    for c in range(1, p // 2):
        for a in range(1, (p - c) // 2):
            b = p - c - a
            if is_right_triangle(a, b, c):
                sols[p].append((a, b, c))

print(max(sols, key=lambda x: len(sols[x])))

