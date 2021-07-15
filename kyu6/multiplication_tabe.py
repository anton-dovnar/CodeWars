def multiplication_table(size):
    table = []

    for row in range(1, size + 1):
        next_value = row
        table.append([next_value])
        for column in range(size-1):
            next_value += row
            table[row-1].append(next_value)
    return table
