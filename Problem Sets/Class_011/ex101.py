def process_data(lst):
    res = []

    for i in range(len(lst)-1):
        try:
            res.append(int(lst[i] + lst[i+1]))
        except (TypeError, ValueError):
            pass
    return res
