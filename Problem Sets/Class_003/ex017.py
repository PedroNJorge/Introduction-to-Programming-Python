n = int(input())
result = ""

for i in range(1, 100+1):
    if i % n == 0:
        result += str(i) + " "
print(result[:-1])
