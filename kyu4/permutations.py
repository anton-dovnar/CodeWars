from itertools import permutations as perm


def permutations(string):
    return set([''.join(variation) for variation in perm(string)])
