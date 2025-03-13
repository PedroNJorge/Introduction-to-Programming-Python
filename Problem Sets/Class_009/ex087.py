def func(lst, cur, k, planets):
    if k == 0:
        lst.append(cur)
    else:
        for i in planets:
            func(lst, cur + [i], k-1, planets)


def weekends(k, planets):
    lst = []
    func(lst, [], k, planets)

    return lst
