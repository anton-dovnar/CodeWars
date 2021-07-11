from collections import Counter


def is_valid_walk(walk):
    opposite_directions = {
        'n': 's',
        's': 'n',
        'w': 'e',
        'e': 'w'
    }
    points = Counter(walk)
    for key, value in points.items():
        if points[opposite_directions[key]] != value:
            return False
    return sum(points.values()) == 10
