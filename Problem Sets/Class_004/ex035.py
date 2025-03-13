from math import ceil


def mean(a, b):
    return (a+b)/2


def digits_average(n):
    n = str(n)

    while len(n) != 1:
        m = ""
        for i in range(len(n)-1):
            m += str(ceil(mean(int(n[i]), int(n[i+1]))))
        n = m

    return int(n)
#
# n = int(input())
# print(digits_average(n))
