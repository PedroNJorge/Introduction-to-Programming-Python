def swap_list(lst):
    for i in range(1, len(lst), 2):
        a = lst[i]
        lst[i] = lst[i-1]
        lst[i-1] = a


'''
lst1 = ['a','b','c','d','e','f']
swap_list(lst1)
print(lst1)
lst2 = [1,2,3,4,5,6,7,8,9]
swap_list(lst2)
print(lst2)
'''
