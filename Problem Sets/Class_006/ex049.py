def fibonacci(a, b, n):
    lst = [a, b]

    for i in range(2, n):
        lst.append(lst[i-1] + lst[i-2])

    return lst


'''
print(fibonacci(0,1,13))
print(fibonacci(2,4,10))
print(fibonacci(1,3,12))
'''
