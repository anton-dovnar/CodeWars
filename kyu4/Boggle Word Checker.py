def find_next_letters(board, row_index, col_index, word, index, visited):
    if index == len(word):
        return True

    if (
        row_index < 0 or row_index >= len(board) or
        col_index < 0 or col_index >= len(board[0]) or
        visited[row_index][col_index] or
        board[row_index][col_index] != word[index]
    ):
        return False

    visited[row_index][col_index] = True

    found = any(
        find_next_letters(board, x, y, word, index + 1, visited)
        for x in range(row_index - 1, row_index + 2)
        for y in range(col_index - 1, col_index + 2)
        if (x, y) != (row_index, col_index)
    )

    visited[row_index][col_index] = False
    return found

def find_word(board, word):
    visited = [[False] * len(board[0]) for _ in range(len(board))]

    for row_index in range(len(board)):
        for col_index in range(len(board[0])):
            if board[row_index][col_index] == word[0]:
                if find_next_letters(board, row_index, col_index, word, 0, visited):
                    return True
    return False
