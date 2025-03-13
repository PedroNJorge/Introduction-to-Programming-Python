n = int(input())
rs = " "*(n-1) + "1"

for i in range(2, n+1):
    rs += "\n" + " "*(n-i)
    for k in range(1, i+1):
        rs += str(k)
    for j in range(i-1, 0, -1):
        rs += str(j)
print(rs)
