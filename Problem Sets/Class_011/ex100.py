import random


def find_exit(connections, check_booth, seed):
    rng = random.Random(seed)
    dic = connections.copy()

    for i in connections.keys():
        if rng.random() < 0.30:
            del dic[i]
    try:
        return dic[check_booth]
    except KeyError:
        return "Compromised booth! Aborting connection."
