potential_coins = [200, 100, 50, 20, 10, 5, 2, 1]
ways = {}

def ways_to_make_amount(amount, largest_coin_allowed):
    if (amount, largest_coin_allowed) in ways:
        return ways[(amount, largest_coin_allowed)]

    if amount == 0:
        return 1
    elif amount < 0:
        return 0

    allowed_coins = [c for c in potential_coins if c <= largest_coin_allowed]
    result = 0
    for c in allowed_coins:
        result += ways_to_make_amount(amount - c, c)

    ways[(amount, largest_coin_allowed)] = result
    return result

print(ways_to_make_amount(200, 200))


