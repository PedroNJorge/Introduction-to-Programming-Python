def remove_non_ch(needle, haystack):
    new = ""
    for i in haystack:
        if i in needle:
            new += i
    return new


def substring(needle, haystack):
    haystack = remove_non_ch(needle, haystack)

    for i in needle:
        if i in haystack:
            haystack = haystack[haystack.index(i) + 1:]
        else:
            return False

    return True
