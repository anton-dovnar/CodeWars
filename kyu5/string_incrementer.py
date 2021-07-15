import re


def increment_string(string):
    match = re.search('\d+$', string)
    if match:
        return re.sub(r'(\d+)$', lambda n: str(int(n.group(1)) + 1).zfill(len(n.group(1))), string)
    else:
        return string + '1'
