# Sort of similar to long division, looking for repeated accumulators

def len_period(n):
    accs = [10]
    while True:
        acc = (accs[-1] % n) * 10
        if acc in accs:
            break
        accs.append(acc)
    return len(accs) - accs.index(acc)

periods = [(n, len_period(n)) for n in range(1, 1001)]
print(max(periods, key=lambda pair: pair[1]))

