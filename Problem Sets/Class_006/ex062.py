def spiral_number(y, x):
    if y == x:
        return (y**2 - y + 1)
    elif y > x:
        return (y**2 - y + 1 + (y-x)*(-1)**y)
    else:
        return (x**2 - x + 1 + (x-y)*(-1)**(x+1))


'''
print(spiral_number(1,1))
print(spiral_number(1,2))
print(spiral_number(1,3))
print(spiral_number(1,4))
print(spiral_number(1,5))

print(spiral_number(2,1))
print(spiral_number(2,2))
print(spiral_number(2,3))
print(spiral_number(2,4))
print(spiral_number(2,5))

print(spiral_number(3,1))
print(spiral_number(3,2))
print(spiral_number(3,3))
print(spiral_number(3,4))
print(spiral_number(3,5))

print(spiral_number(4,1))
print(spiral_number(4,2))
print(spiral_number(4,3))
print(spiral_number(4,4))
print(spiral_number(4,5))

print(spiral_number(5,1))
print(spiral_number(5,2))
print(spiral_number(5,3))
print(spiral_number(5,4))
print(spiral_number(5,5))

print(spiral_number(121998376,943430501))
print(spiral_number(689913499,770079066))
print(spiral_number(586095107,933655238))
print(spiral_number(704012672,608536365))
print(spiral_number(982851657,940887637))
'''
