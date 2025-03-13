def word_types(lst):
    dic = {"lower": 0, "upper": 0, "other": 0}

    for i in lst:
        if i == i.lower():
            dic["lower"] += 1
        elif i == i.upper():
            dic["upper"] += 1
        else:
            dic["other"] += 1
    return (dic["lower"], dic["upper"], dic["other"])
