from collections import Counter


def anagrams(word, words):
    allowed_chars = Counter(word)
    result = []
    for w in words:
        c = Counter(w)
        c.subtract(allowed_chars)
        if all(v == 0 for v in c.values()):
            result.append(w)
    return result
