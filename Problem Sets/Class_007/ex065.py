def swap(menu):
    new = {}
    for key, value in menu.items():
        new[value] = key
    return new
