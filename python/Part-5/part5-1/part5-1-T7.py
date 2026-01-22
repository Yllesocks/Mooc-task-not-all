def row_correct(sudoku: list, row_no: int):
    seen = set()
    for value in sudoku[row_no]:
        if value == 0:
            continue
        if value < 1 or value > 9 or value in seen:
            return False
        seen.add(value)
    return True


def column_correct(sudoku: list, column_no: int):
    seen = set()
    for row in sudoku:
        value = row[column_no]
        if value == 0:
            continue
        if value < 1 or value > 9 or value in seen:
            return False
        seen.add(value)
    return True


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


def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if not row_correct(sudoku, i):
            return False
        if not column_correct(sudoku, i):
            return False

    for row in (0, 3, 6):
        for col in (0, 3, 6):
            if not block_correct(sudoku, row, col):
                return False

    return True