def swap(word):
    new = ""
    l = len(word)

    if l % 2 == 0:
        for i in range(0, l, 2):
            new += word[i + 1] + word[i]
    else:
        for i in range(0, l - 1, 2):
            new += word[i + 1] + word[i]
        new += word[-1]

    return new
