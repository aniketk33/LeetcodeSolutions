def change_to_zeroes(matrix):
    rows, columns = len(matrix), len(matrix[0])
    # for (0,0) position element
    first_element_zero = False

    # find the check points for which rows/columns to change to zeroes
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 0:
                # change the first value for that particular column to zero
                matrix[0][c] = 0
                if r == 0:
                    first_element_zero = True
                else:
                    # change the first value for that particular row to zero
                    matrix[r][0] = 0

    # convert to zero except for the 0th row/column
    for r in range(1, rows):
        for c in range(1, columns):
            # check if the 0th position is zero or not for both rows and columns
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # first change the first column to zero
    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0

    # convert the first row to zero
    if first_element_zero:
        for c in range(columns):
            matrix[0][c] = 0


grid = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(grid)
change_to_zeroes(grid)
print(grid)
