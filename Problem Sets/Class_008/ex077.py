def count_words(text):
    return len({x.lower() for x in text.split(" ") if len(x) > 0})
