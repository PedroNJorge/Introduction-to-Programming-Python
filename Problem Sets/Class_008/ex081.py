def sort_initials(text):
    first_letters = sorted([x[0] for x in text.lower().split(" ")])
    count_letters = [(first_letters.count(x), x) for x in first_letters]
    strd = sorted(count_letters, key=lambda x: (-x[0], x[1]))
    result = ""

    for i in strd:
        if i[1] not in result:
            result += i[1]
    return result
