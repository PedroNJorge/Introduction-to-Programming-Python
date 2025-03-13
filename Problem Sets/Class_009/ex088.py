def func(lst, cur, coins):
    lst.add(sum(cur))
    if coins:
        for i, v in enumerate(coins):
            func(lst, cur + [v], coins[i+1:])


def quantities(coins):
    lst = set()
    func(lst, [], coins)

    return lst
