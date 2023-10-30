def island_perimeter(grid):
    ROWS, COLUMNS = len(grid), len(grid[0])
    visited_positions = set()

    def dfs(curr_row, curr_column):
        # if it is water or boundary then return 1
        if (curr_row < 0 or curr_column < 0 or curr_row == ROWS or curr_column == COLUMNS
                or grid[curr_row][curr_column] == 0):
            return 1

        # already visited positions will return 0
        if (curr_row, curr_column) in visited_positions:
            return 0

        visited_positions.add((curr_row, curr_column))
        # get all the adjacent values of given coordinate
        perimeter = dfs(curr_row, curr_column + 1)
        perimeter += dfs(curr_row, curr_column - 1)
        perimeter += dfs(curr_row + 1, curr_column)
        perimeter += dfs(curr_row - 1, curr_column)

        return perimeter

    for row in range(ROWS):
        for column in range(COLUMNS):
            # traverse only when it is a land
            if grid[row][column] == 1:
                return dfs(row, column)


input_grid = [[0, 1]]
res = island_perimeter(input_grid)
print(res)
