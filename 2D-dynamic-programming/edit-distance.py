def min_distance(word1, word2):
    grid = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    # fill the grid with base cases
    # for the last row, we have to move column wise
    last_row = len(word1)
    for column in range(len(word2) + 1):
        grid[last_row][column] = len(word2) - column
    last_column = len(word2)
    for row in range(len(word1) + 1):
        grid[row][last_column] = len(word1) - row

    # iteration from the second last row and column position
    for row in range(last_row - 1, -1, -1):
        for column in range(last_column - 1, -1, -1):
            if word1[row] == word2[column]:
                # assign the diagonal value
                grid[row][column] = grid[row + 1][column + 1]
            else:
                # all three cases .i.e. get the min from the right, bottom, and diagonal
                grid[row][column] = 1 + min(grid[row][column + 1], grid[row + 1][column], grid[row + 1][column + 1])

    return grid[0][0]


res = min_distance('abd', 'acd')
print(res)
