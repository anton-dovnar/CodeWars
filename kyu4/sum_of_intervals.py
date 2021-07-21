def sum_of_intervals(intervals):
    unique_range = set()

    for start, stop in intervals:
        current = start
        while current < stop:
            unique_range.add(current)
            current += 1

    return len(unique_range)
