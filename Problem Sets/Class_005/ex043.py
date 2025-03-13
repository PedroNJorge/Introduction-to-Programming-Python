def search(tup, value):
    
    if value not in tup:
        return (-1, -1)

    tf = list(map(lambda x: x == value, tup))
    a = 0
    b = 0
    n = len(tf)

    for i, v in enumerate(tf):
        if v:
            a = i
            break
    
    for i in range(-1, -n, -1):
        if tf[i]:
            b = n + i
            break
    return (a, b)
