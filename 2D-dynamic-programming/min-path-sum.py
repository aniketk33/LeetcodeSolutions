def min_path_sum(grid):
    rows, columns = len(grid), len(grid[0])
    bottom_row = [float('inf')] * (columns + 1)
    bottom_row[columns-1] = 0

    for row in range(rows - 1, -1, -1):
        for column in range(columns - 1, -1, -1):
            bottom_value = bottom_row[column]
            right_value = bottom_row[column+1]
            bottom_row[column] = grid[row][column] + min(bottom_value, right_value)

    return bottom_row[0]


res = min_path_sum([[1, 2, 3], [4, 5, 6]])
print(res)
