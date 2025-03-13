def pascal(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        line = [1]
        prev_line = pascal(n-1)
        prev = 1
        for i in range(1, len(prev_line)):
            line.append(prev + prev_line[i])
            prev = prev_line[i]
        line.append(1)
        return line


'''
print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))
print(pascal(5))
'''
