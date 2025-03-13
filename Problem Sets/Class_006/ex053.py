def occurrences(lst, x):
    new = []

    for i, v in enumerate(lst):
        if v == x:
            new.append(i)
    return new
