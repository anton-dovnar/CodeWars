def find_missing(sequence):
    minimum_difference = float('inf')

    for idx in range(len(sequence) - 1):
        difference = abs(sequence[idx+1] - sequence[idx])
        if difference < minimum_difference:
            minimum_difference = difference

    for idx in range(1, len(sequence)):
        if abs(sequence[idx] - sequence[idx-1]) > minimum_difference:
            return sequence[idx] - (minimum_difference * -1 if sequence[idx] < 0 else minimum_difference)
