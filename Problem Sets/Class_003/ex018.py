n = int(input())
sum = 0

for i in range(1, n+1):
    sum += 50/i
    print(f"Night {i}: {round(50/i, 2)}E")

print(f"Total: {round(sum, 2)}E")
