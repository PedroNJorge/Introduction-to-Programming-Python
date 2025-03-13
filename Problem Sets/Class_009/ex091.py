def rec(lst, cur, friends, k, enemies):
    if k == 0:
        lst.append(cur)
    else:
        for i, v in enumerate(friends):
            rec(lst, cur + [v], friends[i+1:], k-1, enemies)


def dinner(friends, k, enemies):
    lst = []
    rec(lst, [], friends, k, enemies)
    for x, y in enemies:
        lst = [sorted(L) for L in lst if not (x in L and y in L)]
    return lst
