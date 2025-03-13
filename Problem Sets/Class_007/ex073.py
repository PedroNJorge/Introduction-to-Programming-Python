def possible(digits, a, b):
    n = 0
    for i in range(a, b + 1):
        condition = True
        for j in str(i):
            if j not in digits:
                condition = False
                break
        if condition:
            n += 1
    return n
