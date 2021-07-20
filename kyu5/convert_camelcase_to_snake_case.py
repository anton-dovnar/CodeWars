import re


def to_underscore(string):
    if isinstance(string, int):
        return str(string)
    return '_'.join(re.sub(r"([A-Z])", ' \g<1>', string).strip().lower().split())
