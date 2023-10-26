def max_area(grid):
    ROWS, COLUMNS = len(grid), len(grid[0])
    visited_positions = set()

    def dfs(curr_row, curr_column):
        # base cases
        if (curr_row < 0 or curr_row == ROWS or curr_column < 0 or curr_column == COLUMNS
                or grid[curr_row][curr_column] == 0 or (curr_row, curr_column) in visited_positions):
            return 0

        # if it is island then add to the visited set and
        visited_positions.add((curr_row, curr_column))

        # recursive call to all the adjacent positions of the grid
        return (1 + dfs(curr_row + 1, curr_column) + dfs(curr_row - 1, curr_column) +
                dfs(curr_row, curr_column + 1) + dfs(curr_row, curr_column - 1))

    area = 0
    for row in range(ROWS):
        for column in range(COLUMNS):
            area = max(area, dfs(row, column))

    return area


input_grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
res = max_area(input_grid)
print(res)
