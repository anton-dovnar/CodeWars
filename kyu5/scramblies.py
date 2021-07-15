from collections import Counter


def scramble(s1, s2):
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)
    return not (s2_counter - s1_counter)
