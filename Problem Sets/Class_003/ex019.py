r1 = float(input())
x1 = float(input())
y1 = float(input())
r2 = float(input())
x2 = float(input())
y2 = float(input())

d = ((x1-x2)**2 + (y1-y2)**2)**0.5
p = "The circles are tangent."
q = "The circles are not tangent."

if r1 >= d or r2 >= d:
    if d + r2 == r1 or d + r1 == r2:
        print(p)
    else:
        print(q)
else:
    if r1 + r2 == d:
        print(p)
    else:
        print(q)
