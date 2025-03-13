def highest_items(menu):
    high = []
    high_order = sorted(menu.items(), key=lambda x: x[1], reverse=True)
    max = high_order[0][1]
    for k, v in high_order:
        if v == max:
            high.append(k)
        else:
            break
    return high
