from operator import itemgetter


def sum_pairs(ints, s):
    hashtable = set(ints)
    pairs = [] # Pairs (index, vlaue)
    # Determin closest elements by indexes
    closest = float('inf'), 0 # First argument difference between indexes, Second - index in pairs array

    for index, number in enumerate(ints):
        difference = s - number
        if difference in hashtable:
            try:
                pair = [(index, number),  (ints[index+1:].index(difference) + index + 1, difference)]
            except ValueError:
                print(f'Difference {difference} is not in list')
            else:
                pairs.append(pair)

    first_term_of_sum = itemgetter(0)
    second_term_of_sum = itemgetter(1)
    get_index = itemgetter(0)
    get_value = itemgetter(1)

    for key, pair in enumerate(pairs):
        index1 = get_index(first_term_of_sum(pair))
        index2 = get_index(second_term_of_sum(pair))
        diff = index2 - index1
        if diff < closest[0]:
            closest = diff, key

    return [
        get_value(first_term_of_sum(pairs[closest[1]])),
        get_value(second_term_of_sum(pairs[closest[1]]))
    ] if pairs else None
