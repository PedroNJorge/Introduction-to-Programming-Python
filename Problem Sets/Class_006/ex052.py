def unique(lst):
    uniq = []
    seen = {}

    for i in lst:
        if i in seen.keys():
            seen[i] += 1
        else:
            seen[i] = 1

    for i in seen.keys():
        if seen[i] == 1:
            uniq.append(i)

    return uniq


'''
print(unique(["bart","lewis","bart", "martin", "bart", "nelson","martin"]))
print(unique(['a','b','c','d']))
print(unique([True, False, True, False]))
print(unique(['f', 'o', 'r', 't', 'y', 't', 'w', 'o']))
'''
