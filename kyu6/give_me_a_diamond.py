def diamond(n):
    if n < 0 or n % 2 == 0:
        return None

    diamond = []
    for i in range(1, n // 2 + 2):
        row = '*' * (i * 2 - 1)
        extra_space = (n - len(row)) // 2
        diamond.append(' ' * extra_space + row + '\n')
    diamond.extend(reversed(diamond[:-1]))
    return "".join(diamond)
