def extremes(words):
    a = len(words[0])
    b = a

    for i in words[1:]:
        if len(i) < a:
            a = len(i)
        elif len(i) > b:
            b = len(i)

    return (a, b)
