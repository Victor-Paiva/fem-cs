def make_change(amount, coins):
    coins.sort(reverse=True)
    change = []

    i = 0
    while amount > 0:
        if coins[i] <= amount:
            amount -= coins[i]
            change.append(coins[i])
        else:
            i += 1
            if i == len(coins):
                return None

    return change

coins = [5, 10, 25]
change = make_change(62, coins)
print(change)