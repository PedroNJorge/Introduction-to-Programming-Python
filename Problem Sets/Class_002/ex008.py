s_h = int(input())
s_m = int(input())
s_s = int(input())
b_h = int(input())
b_m = int(input())
b_s = int(input())

MM = s_m + b_m
HH = s_h + b_h
SS = s_s + b_s

MM += SS // 60
SS -= 60*(SS//60)

HH += MM // 60
MM -= 60*(MM//60)

HH -= 24*(HH//24)

if HH <= 9:
    HH = "0"+str(HH)
if MM <= 9:
    MM = "0"+str(MM)
if SS <= 9:
    SS = "0"+str(SS)

print(f"Take the cake out at {HH}:{MM}:{SS}.")
