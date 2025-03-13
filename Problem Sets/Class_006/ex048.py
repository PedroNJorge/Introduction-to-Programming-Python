def transform(lst, k):
    lst[:] = map(lambda x: x*k, lst)


'''
lst = [1,2,3,4,5]
transform(lst, 2)
print(lst)
transform(lst, 5)
print(lst)
'''
