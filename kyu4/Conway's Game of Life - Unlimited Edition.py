def get_living_neighbours(cells: list[list[int]], row_index: int, col_index: int) -> int:
    return sum(
        cells[x][y]
        for x in range(row_index - 1, row_index + 2)
        for y in range(col_index - 1, col_index + 2)
        if (0 <= x < len(cells) and 0 <= y < len(cells[0]) and (x, y) != (row_index, col_index))
    )


def clean_empty_x_y(result: list[list[int]]) -> None:
    while result and all(cell == 0 for cell in result[0]):
        result.pop(0)

    while result and all(cell == 0 for cell in result[-1]):
        result.pop()

    while result and all(row[0] == 0 for row in result):
        for row in result:
            row.pop(0)

    while result and all(row[-1] == 0 for row in result):
        for row in result:
            row.pop()


def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:
    if generations == 0:
        return cells

    origin = [[0] * (len(cells[0]) + 2)] + [[0] + row + [0] for row in cells] + [[0] * (len(cells[0]) + 2)]
    result = [[0] * len(origin[0]) for _ in range(len(origin))]
    
    for row_index in range(len(origin)):
        for col_index in range(len(origin[0])):
            live_neighbours = get_living_neighbours(origin, row_index, col_index)

            if origin[row_index][col_index]:
                result[row_index][col_index] = 1 if 2 <= live_neighbours <= 3 else 0
            else:
                result[row_index][col_index] = 1 if live_neighbours == 3 else 0
                    
    clean_empty_x_y(result)
    return get_generation(result, generations - 1) if generations > 1 else result


if __name__ == "__main__":
    cells = [
        [1,1,1,0,0,0,1,0],
        [1,0,0,0,0,0,0,1],
        [0,1,0,0,0,1,1,1]
    ]
    generations = 16
    result = get_generation(cells, generations)
    assert result == [
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]
    ]
