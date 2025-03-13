def rec(lst, cur, planets):
    if len(cur) == len(planets):
        lst.append(cur + [cur[0]])
    else:
        for i, v in enumerate(planets):
            if v not in cur:
                rec(lst, cur + [v], planets)


def visit(planets):
    lst = []
    rec(lst, [], planets)
    return lst
