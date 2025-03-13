from math import ceil


def show_table(k, lst):
    width = max(map(len, lst))
    sep = ("+"+"-"*width)*k + "+"
    L = len(lst)

    for i in range(ceil(L / k)):
        print(sep)
        for j in range(k):
            if j < len(lst):
                print("|" + " "*(width - len(lst[j])) + lst[j], end="")
            else:
                print("|" + " "*width, end="")
        print("|")
        lst = lst[j+1:]
    print(sep)
