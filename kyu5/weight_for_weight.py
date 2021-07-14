from operator import add
from functools import reduce

def order_weight(string):
    weight_scores = [] # First argument score, Second argument original weight

    for weight in string.split():
        weight_scores.append([reduce(add, map(int, weight)), weight])

    weight_scores.sort(key=lambda x: (x[0], x[1]))
    return ' '.join([weight for score, weight in weight_scores])
