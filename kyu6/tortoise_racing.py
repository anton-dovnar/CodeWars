def race(v1, v2, g):
    if v1 >= v2:
        return None

    time = g * 3600 // (v2 - v1)
    return [time // 3600, time % 3600 // 60, time % 60]
