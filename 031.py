# Bucket stores number of ways to create type of currency

bucket = {}
bucket[1] = 1

potential_coins = [1, 2, 5, 10, 20, 50, 100, 200]

def largest_coins(goal, potential_coins):
    result = []
    for coin in potential_coins[::-1]:
        while goal - coin >= 0:
            result.append(coin)
            goal = goal - coin

    return result

assert(largest_coins(1, potential_coins) == [1])
assert(largest_coins(10, potential_coins) == [10])
assert(largest_coins(37, potential_coins) == [20, 10, 5, 2])
assert(largest_coins(4, potential_coins) == [2, 2])
