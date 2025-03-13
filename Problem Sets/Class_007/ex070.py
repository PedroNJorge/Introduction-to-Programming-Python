def possible_sums(coins):
    s1, s2, s3 = set(), set(), set()
    for i in coins:
        s1.add(i)
        for j in coins:
            s2.add(i+j)
            for k in coins:
                s3.add(i+j+k)
        s1 |= s1
        s2 |= s2
        s3 |= s3

    return s1 | s2 | s3
