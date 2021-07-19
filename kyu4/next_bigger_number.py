def next_bigger(n):
    max_order = get_max_order(n)

    for i in range(n + 1, max_order + 1):
        if get_max_order(i) == max_order:
            return i
    return -1


def get_max_order(number):
    return int(''.join(sorted(list(str(number)), reverse=True)))
