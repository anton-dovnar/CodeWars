def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    return sorted(list(map(lambda a: a * a, array1))) == sorted(array2)
