def compose(f, g):
    h = {}

    for key, value in f.items():
        if f[key] in g.keys():
            h[key] = g[f[key]]

    return h
