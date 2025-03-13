num = int(input())
factors = "1"
sum = 1

for i in range(2, num):
    if num % i == 0:
        factors = str(i) + " " + factors
        sum += i

if sum != num:
    print(f"{num} is not a perfect number")
else:
    print(f"{num} is a perfect number")
    print(f"Factors: {factors}")
