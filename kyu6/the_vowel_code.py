import re


VOWEL_CODE = {
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5',
}

NUMERIC_CODE = {
    '1': 'a',
    '2': 'e',
    '3': 'i',
    '4': 'o',
    '5': 'u',
}


def encode(st):
    return re.sub(r'([aeiou])', lambda x: VOWEL_CODE[x.group(1)], st)

def decode(st):
    return re.sub(r'([1-5])', lambda x: NUMERIC_CODE[x.group(1)], st)
