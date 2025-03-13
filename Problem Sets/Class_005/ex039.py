def duplicate(tup):
    new = []

    for i in tup:
        new.append(i)
        new.append(i)

    return tuple(new)
