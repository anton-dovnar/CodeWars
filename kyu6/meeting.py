import re
from operator import itemgetter


def meeting(s):
    names = re.findall(r'\w+', s)
    name_groups = []
    for i in range(0, len(names) - 1, 2):
        name_groups.append([names[i+1].upper() ,names[i].upper()])

    name_groups.sort(key=lambda x: (itemgetter(0)(x), itemgetter(1)(x)))
    return ''.join([f'({last_name}, {first_name})' for last_name, first_name in name_groups])
