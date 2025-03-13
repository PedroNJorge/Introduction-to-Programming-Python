def extract_numbers(text):
    num = ""
    lst = []
    for i in text:
        if 48 <= ord(i) <= 57:
            num += i
        elif len(num) > 0:
            lst.append(int(num))
            num = ""

    if len(num) > 0:
        lst.append(int(num))

    return lst
