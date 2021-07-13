import re


def to_weird_case(string):
    return re.sub(r'(\w)([^\s]?[\s]?)', lambda x: x.group(1).upper() + x.group(2), string)
