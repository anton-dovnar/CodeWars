from operator import itemgetter


def namelist(names):
    name_getter = itemgetter('name')
    list_of_names = [name_getter(name) for name in names]
    if len(list_of_names) < 2:
        return ''.join(list_of_names)
    return ', '.join(list_of_names[:-1]) + f" & {list_of_names[-1]}"
