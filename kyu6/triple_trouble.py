from collections import Counter


def triple_double(num1, num2):
    occurrences_num1 = Counter(list(str(num1)))
    occurrences_num2 = Counter(list(str(num2)))
    counter = 0

    for key, value in occurrences_num1.items():
        if value >= 3 and occurrences_num2[key] >= 2:
            counter += 1
    return counter
