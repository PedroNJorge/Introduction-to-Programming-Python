def vigenere(text, keyword, mode):
    if mode == "E":
        n = 0
    else:
        n = 1

    text = list(map(lambda ch: ord(ch) if 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122 else ch, text))
    keyword = [ord(x) - 97 for x in keyword]
    L = len(keyword)

    for i in range(len(text)):
        ch = text[i]
        if isinstance(ch, int):
            if 65 <= ch <= 90:
                text[i] = chr((text[i] + keyword[i % L]*(-1)**n - 65) % 26 + 65)
            else:
                text[i] = chr((text[i] + keyword[i % L]*(-1)**n - 97) % 26 + 97)
    return "".join(text)


def vigenere_encrypt(text, keyword):
    return vigenere(text, keyword, "E")


def vigenere_decrypt(text, keyword):
    return vigenere(text, keyword, "D")
