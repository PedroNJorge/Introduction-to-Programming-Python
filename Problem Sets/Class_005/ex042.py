def count(word, letters):
    counter = 0
    
    for i in word:
        if i in letters:
            counter += 1
    
    return counter
