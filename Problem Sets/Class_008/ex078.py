def caesar_cipher(text, k):
    for i, v in enumerate(str(text)):
        if ord(v) >= 97 and ord(v) <= 122:
            text = text[:i] + chr(((ord(v) + k - 97) % 26) + 97) + text[i+1:]
    return text
