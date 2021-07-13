def tower_builder(n_floors):
    row_length = n_floors * 2 - 1
    number_of_stars = 1
    result = []

    for _ in range(n_floors):
        row = number_of_stars * '*'
        result.append(row.center(row_length))
        number_of_stars += 2
    return result
