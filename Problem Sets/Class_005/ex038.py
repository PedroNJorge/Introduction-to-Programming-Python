def odd_even(tup):
    new = []

    for i in range(0, len(tup), 2):
        new.append(tup[i])

    for i in range(1, len(tup), 2):
        new.append(tup[i])

    return tuple(new)


#n = tuple(input())

#print(odd_even(n))
