import re


def is_valid_IP(string):
    match = re.findall(r'(25[0-5]|[2][0-4][0-9]|[1][0-9][0-9]|[0-9]{2}|[0-9]{1})', string)
    return len(match) == 4 and '.'.join(match) == string
