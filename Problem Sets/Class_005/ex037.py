def palindrome(word):
    lst = ""
    
    for i in word:
        lst = i + lst

    return word == lst
