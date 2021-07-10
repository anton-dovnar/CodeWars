def tribonacci(signature, n):
    if n < 1:
        return []
    elif n < 3:
        return signature[:n]

    length = len(signature)
    cache = signature
    for i in range(n-length):
        next_value = sum(cache[i:i+3])
        cache.append(next_value)
    return cache
