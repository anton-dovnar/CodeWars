from collections import deque


def expanded_form(num):
    double_end_queue = deque()
    pos = 1
    while num:
        last_digit = num % 10
        if last_digit > 0:
            double_end_queue.appendleft(str(last_digit).ljust(pos, '0'))
        pos += 1
        num //= 10
    return ' + '.join(double_end_queue)
