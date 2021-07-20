cache = {0: 0, 1: 1}


def fibonacci(n):
    if n in cache:
        return cache[n]
    else:
        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]
    return cache[n]
