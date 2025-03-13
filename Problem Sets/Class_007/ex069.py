def remove(x, menu):
    for i in list(menu):
        if i[0] == x:
            menu.discard(i)
