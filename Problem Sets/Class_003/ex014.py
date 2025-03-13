import math

menu = input()
r = float(input())

if menu == "1":
    print(f"Diameter: {2*r:.2f}")
elif menu == "2":
    print(f"Perimeter: {2*math.pi*r:.2f}")
elif menu == "3":
    print(f"Area: {math.pi*r**2:.2f}")
else:
    print("Invalid Option.")
