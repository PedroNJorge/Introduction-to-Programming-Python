num = input()
prev = num[0]

ascend, descend = False, False
for i in num[1:]:
    if int(prev) > int(i):
        descend = True
    elif int(prev) < int(i):
        ascend = True
        if descend:
            break
    prev = i

if (ascend and descend):
    order = "not ordered."
elif ascend:
    order = "in ascending order."
elif descend:
    order = "in descending order."
else:
    order = "not ordered."

print(f"The number is {order}")
