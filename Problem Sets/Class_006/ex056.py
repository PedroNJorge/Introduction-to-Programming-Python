def list_to_matrix(lst, r, c):
    m = []
    j = 1
    for i in range(r):
        m.append(lst[(j-1)*c:j*c])
        j += 1
    return m


'''
print(list_to_matrix([1,2,3,4,5,6,7,8,9], 3, 3))
print(list_to_matrix([9,8,7,6,5,4,3,2,1,0], 2, 5))
'''
