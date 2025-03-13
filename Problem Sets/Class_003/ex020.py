import math

a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4*a*c

if delta == 0:
    R1 = -b / (2*a)
    print(f"R = {round(R1, 2)}")
elif delta > 0:
    R1 = (-b + math.sqrt(delta)) / (2*a)
    R2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"R1 = {round(R1, 2)}")
    print(f"R2 = {round(R2, 2)}")
else:
    Real = -b / (2*a)
    Imag = math.sqrt(-delta) / (2*a)
    print(f"R1 = {round(Real, 2)} + {round(Imag, 2)}i")
    print(f"R2 = {round(Real, 2)} - {round(Imag, 2)}i")
