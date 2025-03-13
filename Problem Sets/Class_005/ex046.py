def evolve(initial, n):
    for i in range(n):
        initial = "".join(map(lambda x: "AB" if x == "A" else "A", initial))
        print(initial)
