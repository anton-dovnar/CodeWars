from itertools import chain


def is_solved(board):
    cols = list(zip(*board))
    rows = board
    diag1_arr = []
    diag2_arr = []

    for idx in range(3):
        row_sum = sum(board[idx])
        col_sum = sum(cols[idx])
        diag1_arr.append(board[idx][idx])
        diag2_arr.append(board[idx][2-idx])

        if all(rows[idx]) and row_sum in (3, 6):
            return (1, 0, 0, 2)[row_sum - 3]
        elif all(cols[idx]) and col_sum in (3, 6):
            return (1, 0, 0, 2)[col_sum - 3]

    diag1_sum = sum(diag1_arr)
    diag2_sum = sum(diag2_arr)

    if all(diag1_arr) and diag1_sum in (3, 6):
        return (1, 0, 0, 2)[diag1_sum - 3]
    elif all(diag2_arr) and diag2_sum in (3, 6):
        return (1, 0, 0, 2)[diag2_sum - 3]

    total = sum(chain.from_iterable(board))
    if total == 13:
        return 0

    return -1
