def sum_all_odds(a, b):
    s = 0
    
    for i in range(min(a, b), max(a, b) + 1):
        if i % 2 != 0:
            s += i
    
    return s
