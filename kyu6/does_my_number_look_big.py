def narcissistic(value):
    length = len(str(value))
    return sum(map(lambda x: int(x) ** length, str(value))) == value
