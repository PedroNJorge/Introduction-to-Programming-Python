def rotate(lst, dir):
    if len(lst) > 0:
        if dir == "right":
            lst[:] = [lst[-1]] + lst[:-1]
        else:
            lst[:] = lst[1:] + [lst[0]]


'''
lst = ["pacifier", "teddy", "train", "block", "rabbit"]
rotate(lst, "right")
print(lst)
rotate(lst, "right")
print(lst)
rotate(lst, "left")
print(lst)
empty = []
rotate(empty, "left")
print(empty)
'''
