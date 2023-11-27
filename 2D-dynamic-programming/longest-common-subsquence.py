def lcs(text1, text2):
    # plus 1 to handle the boundary cases
    rows, columns = len(text1) + 1, len(text2) + 1
    grid = [[0 for _ in range(columns)] for _ in range(rows)]

    # starting from the bottom right position
    for row in range(rows - 2, -1, -1):
        for column in range(columns - 2, -1, -1):
            # if both the characters match, then add 1 and move diagonally
            if text1[row] == text2[column]:
                grid[row][column] = 1 + grid[row + 1][column + 1]
            # take the max of right and below values
            else:
                grid[row][column] = max(grid[row][column + 1], grid[row + 1][column])

    return grid[0][0]


res = lcs('abcde', 'ace')
print(res)
