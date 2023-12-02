# using dfs
def unique_paths(grid):
    rows, columns = len(grid), len(grid[0])
    # since the target position is 1
    cache = {(rows - 1, columns - 1): 1}

    def dfs(curr_row, curr_column):
        # base cases
        if curr_row >= rows or curr_column >= columns or grid[curr_row][curr_column] == 1:
            return 0
        if (curr_row, curr_column) in cache:
            return cache[(curr_row, curr_column)]
        # get the addition of right and bottom value
        cache[(curr_row, curr_column)] = dfs(curr_row + 1, curr_column) + dfs(curr_row, curr_column + 1)

        return cache[(curr_row, curr_column)]

    return dfs(0, 0)


# using dynamic programming
def unique_paths_2(grid):
    rows, columns = len(grid), len(grid[0])
    curr_row = [0] * columns
    # the last value will be one, as it is the target position
    curr_row[columns - 1] = 1
    for row in range(rows - 1, -1, -1):
        for column in range(columns - 1, -1, -1):
            # add a zero when an obstacle is present
            if grid[row][column] == 1:
                curr_row[column] = 0
            # add the right value within the boundary
            elif column + 1 < columns:
                curr_row[column] += curr_row[column + 1]

    return curr_row[0]


res = unique_paths_2([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
print(res)
