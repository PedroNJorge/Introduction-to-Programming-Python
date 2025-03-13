def s(lst, size, cur, k):
    if size == 0:
        lst.append(cur)
    else:
        s(lst, size - 1, cur + "0", k)
        if k > 0:
            s(lst, size - 1, cur + "1", k-1)


def binary(a, b, k):
    lst = []

    for i in range(a, b + 1):
        lst_tmp = []
        s(lst_tmp, i, "", k)

        lst += lst_tmp

    return lst
