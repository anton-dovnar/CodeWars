def multiplication_table(rows, cols):
    table = []

    for row in range(1, rows + 1):
        next_value = row
        table.append([next_value])
        for column in range(cols - 1):
            next_value += row
            table[row-1].append(next_value)
    return table
