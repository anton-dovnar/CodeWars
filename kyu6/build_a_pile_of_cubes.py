def find_nb(m: int) -> int:
    total = 0
    n = 0

    while total < m:
        n += 1
        total += n ** 3
    return n if total == m else -1
