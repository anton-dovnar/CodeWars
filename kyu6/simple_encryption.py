from itertools import zip_longest


def decrypt(text, n):
    if not text or n <= 0:
        return text

    mid = len(text) // 2
    list_of_chars = list(text)
    while n:
        temp = []
        for right, left in zip_longest(list_of_chars[mid:], list_of_chars[:mid]):
            if right:
                temp.append(right)
            if left:
                temp.append(left)
        list_of_chars = temp
        n -= 1
    text = ''.join(list_of_chars)
    return text



def encrypt(text, n):
    if not text or n <= 0:
        return text

    while n:
        text = ''.join(text[1::2] + text[0::2])
        n -= 1
    return text
