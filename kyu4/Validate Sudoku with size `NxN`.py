class Sudoku(object):
    def __init__(self, data):
        self.data = data
        self.size = len(data)
        self.subgrid_size = int(self.size ** 0.5)

    def validate(self):
        for x in range(self.size):
            seen_so_far_rows = set()
            seen_so_far_cols = set()

            for y in range(self.size):
                row_val = self.data[x][y]
                col_val = self.data[y][x]

                if isinstance(row_val, bool) or isinstance(col_val, bool):
                    raise ValueError("Invalid value types")

                if (row_val in seen_so_far_rows or col_val in seen_so_far_cols
                    or not (1 <= row_val <= self.size)):
                    raise ValueError("Invalid value in row or column")

                seen_so_far_rows.add(row_val)
                seen_so_far_cols.add(col_val)

        for row in range(0, self.size, self.subgrid_size):
            for col in range(0, self.size, self.subgrid_size):
                seen_so_far_box = set()

                for x in range(row, row + self.subgrid_size):
                    for y in range(col, col + self.subgrid_size):
                        val = self.data[x][y]

                        if val in seen_so_far_box or not (1 <= val <= self.size):
                            raise ValueError("Invalid value in subgrid")

                        seen_so_far_box.add(val)

    def is_valid(self):
        if self.size != len(self.data[0]):
            return False

        if not self.subgrid_size ** 2 == self.size:
            return False

        try:
            self.validate()
        except Exception:
            return False

        return True
