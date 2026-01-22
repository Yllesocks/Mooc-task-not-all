def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    new_grid = [row[:] for row in sudoku]
    new_grid[row_no][column_no] = number
    return new_grid