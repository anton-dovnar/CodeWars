from collections import defaultdict


def delete_nth(order, max_e):
    counter = defaultdict(int)
    result = []

    for number in order:
        if counter[number] < max_e:
            counter[number] += 1
            result.append(number)

    return result
