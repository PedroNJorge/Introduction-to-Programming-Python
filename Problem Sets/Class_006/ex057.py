def sum(a, b):
    n, m = len(a), len(a[0])

    for i in range(n):
        for j in range(m):
            a[i][j] += b[i][j]
    return a


'''
print(sum([[1,2,3],[4,5,6],[7,8,9]],
          [[1,2,3],[4,4,4],[9,8,7]]))
print(sum([[9,8,7,6,5],[4,3,2,1,0]],
          [[2,4,6,8,10],[12,14,16,18,20]]))
'''
