def row_correct(sudoku: list, row_no: int):
    seen = set()
    for value in sudoku[row_no]:
        if value == 0:
            continue
        if value < 1 or value > 9 or value in seen:
            return False
        seen.add(value)
    return True