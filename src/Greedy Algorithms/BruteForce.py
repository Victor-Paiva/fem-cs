def brute_force_change(coins):
    def compute(amount):
        if amount == 0:
            return 0

        min_coins = None
        for coin in coins:
            if amount - coin >= 0:
                min_coins = min(min_coins, compute(amount-coin)) if min_coins is not None else compute(amount-coin)
        
        return min_coins + 1
    return compute

b1 = brute_force_change([1, 6, 10])
print(b1(12))