def largest_sequence(num):
    num = str(num)
    max_counter = 1
    counter = 1
    prev = int(num[0])

    for i in num[1:]:
        if int(i) > prev:
            counter += 1
        else:
            if max_counter < counter:
                max_counter = counter
            counter = 1
        prev = int(i)

    return max(max_counter, counter)


# n = int(input())
# print(largest_sequence(n))
