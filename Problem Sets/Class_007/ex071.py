def frequency(ingredients):
    seen = {}
    for i in ingredients:
        if i not in seen.keys():
            seen[i] = 1
        else:
            seen[i] += 1
    return seen
