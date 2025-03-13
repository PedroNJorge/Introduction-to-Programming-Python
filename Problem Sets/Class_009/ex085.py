def sum_integers(data):
    sum = 0
    for i in data:
        if isinstance(i, int):
            sum += i
        elif not (isinstance(i, str) or isinstance(i, float)):
            sum += sum_integers(i)
    return sum


'''
print(sum_integers([[(4,3)],(((45,[9]))),[(42)],[1,6,8]]))
print(sum_integers(["a",([[2]],[["b"]]),40,[[2.2]]]))
print(sum_integers((1,2,[3],[[4]])))
print(sum_integers(["hello","world"]))
'''
