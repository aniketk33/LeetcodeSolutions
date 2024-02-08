def shift(grid, k):
    # rows and columns
    ROWS, COLUMNS = len(grid), len(grid[0])

    result = [[0] * COLUMNS for _ in range(ROWS)]

    for row in range(ROWS):
        for col in range(COLUMNS):
            # change coordinates from 2D to 1D
            curr_idx = row * COLUMNS + col

            # move the index by k and mod it by total length of the array
            new_idx = (curr_idx + k) % (ROWS * COLUMNS)

            # get the 2D coordinates back by using the new index
            new_row = new_idx // COLUMNS
            new_col = new_idx % COLUMNS

            # assign the value in the new position of the result array
            result[new_row][new_col] = grid[row][col]

    return result


res = shift([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
print(res)
