def surrounded_region(grid):
    ROWS, COLUMNS = len(grid), len(grid[0])

    def capture_zeros(curr_row, curr_column):
        if (curr_row < 0 or curr_row == ROWS or curr_column < 0 or curr_column == COLUMNS or
                grid[curr_row][curr_column] != 'O'):
            return

        grid[curr_row][curr_column] = 'T'
        capture_zeros(curr_row + 1, curr_column)
        capture_zeros(curr_row - 1, curr_column)
        capture_zeros(curr_row, curr_column + 1)
        capture_zeros(curr_row, curr_column - 1)

    # 1. capture the border zeros. border condition can be
    # checked if it is located at first row or column or last row or column.
    for row in range(ROWS):
        for column in range(COLUMNS):
            if (grid[row][column] == 'O' and
                    (row in [0, ROWS - 1] or column in [0, COLUMNS - 1])):
                capture_zeros(row, column)

    # 2. change all the zero's in between the grid to X
    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] != 'O':
                continue
            grid[row][column] = 'X'

    # 3. change back the T's to 0's
    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] != 'T':
                continue
            grid[row][column] = 'O'


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
surrounded_region(board)
print(board)
