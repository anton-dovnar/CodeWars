def parts_sums(ls):
    if not ls:
        return [0]

    total = sum(ls)
    result = [total]
    for number in ls:
        total -= number
        result.append(total)
    return result
