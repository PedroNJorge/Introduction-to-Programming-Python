def super_swap(menu):
    new = {}
    for key, value in menu.items():
        if value not in new.keys():
            new[value] = set([key])
        else:
            new[value] |= set([key])
    return new
