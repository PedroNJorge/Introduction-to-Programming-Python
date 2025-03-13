def nested_exceptions(tree):
    lst = []
    for f in tree:
        if isinstance(f, tuple):
            lst.append(nested_exceptions(f))
        else:
            try:
                f()
                lst.append(False)
            except:
                lst.append(True)
    return tuple(lst)
