def make_change(coins):
    cache = {}
    def compute(amount):
        if amount <= 0:
            return 0

        if amount in cache:
            return cache[amount]

        min_coins = None
        for coin in coins:
            if amount - coin >= 0:
                num = compute(amount - coin)
                min_coins = min(min_coins, num) if min_coins is not None else num

        cache[amount] = min_coins + 1
        return cache[amount]

    return compute

coins = [1, 6, 10]
amount = 12

change = make_change(coins)
print(change(12))