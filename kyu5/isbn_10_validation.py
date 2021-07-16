import re


def valid_ISBN10(isbn):
    match = re.match(r'^\d+X?$', isbn)
    if not match or match.end() - match.start() != 10:
        return False

    counter = 0
    for key, value in enumerate(list(match.group()), 1):
        if value == 'X':
            value = 10
        counter += key * int(value)
    return counter % 11 == 0
