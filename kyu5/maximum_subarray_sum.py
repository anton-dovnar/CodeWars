"""
Kadane's Algorithm
"""


def max_sequence(arr):
    max_so_far = 0
    max_so_end = 0
    for number in arr:
        max_so_end += number
        max_so_end = max(max_so_end, number)
        max_so_far = max(max_so_end, max_so_far)
    return max_so_far
