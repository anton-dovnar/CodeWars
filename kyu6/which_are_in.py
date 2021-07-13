import re


def in_array(array1, array2):
    words = ' '.join(array2)
    arr = []

    for word in set(array1):
        match = re.search(r'{}'.format(word), words)
        if match:
            arr.append(word)
    return sorted(arr)
