'''
k is a linear combination of the coins
and the minimum number is the number of linearly independant coins
(NOT TRUE)

independant only and create with filter the list of the coefficients

'''


def func(coins, k, L):
    for n in range(1, L + 1):
        coins_tmp = coins.copy()
        for i in coins:
            if k-i in coins:
                return n
            else:
                func(coins_tmp.remove(i), k-i)
    return -1


def minimum_coins(coins, k):
    if k in coins:
        return 1
    coins = {x for x in coins if x < k}
    
    # independant only

    if coins == set():
        return -1

    coins_srtd = sorted(coins, reverse=True)
    print(coins_srtd, type(coins_srtd))

    return func(coins_srtd, k, L=len(coins_srtd))

print(minimum_coins({1,5,7}, 11))
print(minimum_coins({1,5,10}, 10))
print(minimum_coins({3,6}, 10))
print(minimum_coins({1}, 42))
