def find_all(keyword, text):
    L = len(keyword)
    occ = []

    for i, ch in enumerate(text):
        if ch == keyword[0]:
            if text[i: i+L] == keyword:
                occ.append(i)
    return occ
