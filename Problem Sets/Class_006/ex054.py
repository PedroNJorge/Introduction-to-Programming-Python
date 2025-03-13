def middle(lst):
    n = len(lst)
    lst.sort()
    if n % 2 == 0:
        return [lst[(n // 2) - 1], lst[n // 2]]

    else:
        return [lst[n // 2]]


'''
print(middle(['StAndrew','StJames','StJohn','StPeter','StPhilip']))
print(middle([1,2,3,4,5,6,7,8]))
print(middle([1,9,3,5,7]))
print(middle([8,4,6,2,12,10]))
'''
