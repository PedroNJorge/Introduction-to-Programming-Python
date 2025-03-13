p = float(input())
t = input()

d = 0
tax = 0
if t == "P":
    tax = 0.06
else:
    if p > 200:
        d = 0.10
    elif p >= 50:
        d = 0.05
    else:
        d = 0.02

final_price = round(p*(1 + tax - d), 3)
print(f"Customer: {t} | Price: {final_price}")
