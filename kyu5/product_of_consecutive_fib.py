def productFib(prod):
    if prod == 0:
        return [0, 1, True]

    cache = {0: 0, 1: 1}
    for i in range(2, max(prod, 5)):
        cache[i] = cache[i-1] + cache[i-2]
        previous = cache[i-1]
        current = cache[i]
        if previous * current == prod:
            return [previous, current, True]
        elif previous * current > prod:
            return [previous, current, False]
