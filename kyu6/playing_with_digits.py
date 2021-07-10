import math


def dig_pow(n, p):
    digit_sum = sum(math.pow(int(value), key) for key, value in enumerate(str(n), p))
    k = digit_sum / n
    return k if math.floor(k) == math.ceil(k) else -1
