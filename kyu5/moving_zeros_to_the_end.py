def move_zeros(array):
    non_zeros = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[non_zeros], array[i] = array[i], array[non_zeros]
            non_zeros += 1
    return array
