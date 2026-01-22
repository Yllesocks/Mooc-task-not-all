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