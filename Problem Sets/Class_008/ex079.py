def csv_change(text, a, b):
    splt = text.split(",")
    col1, col2 = splt[a-1], splt[b-1]
    splt[a-1], splt[b-1] = col2, col1
    return ",".join(splt)
