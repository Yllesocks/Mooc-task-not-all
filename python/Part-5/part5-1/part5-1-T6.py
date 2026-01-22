def block_correct(sudoku: list, row_no: int, column_no: int):
    seen = set()
    for row in range(row_no, row_no + 3):
        for column in range(column_no, column_no + 3):
            value = sudoku[row][column]
            if value == 0:
                continue
            if value < 1 or value > 9 or value in seen:
                return False
            seen.add(value)
    return True