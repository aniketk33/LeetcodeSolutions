# recursive solution (top-to-bottom approach)
def maximal_square(matrix):
    rows, columns = len(matrix), len(matrix[0])
    cache = {}

    def dfs(curr_row, curr_col):
        if curr_row >= rows or curr_col >= columns:
            return 0

        if (curr_row, curr_col) not in cache:
            # get the min of bottom, right and diagonal values
            bottom = dfs(curr_row + 1, curr_col)
            right = dfs(curr_row, curr_col + 1)
            diagonal = dfs(curr_row + 1, curr_col + 1)

            if matrix[curr_row][curr_col] == "1":
                cache[(curr_row, curr_col)] = 1 + min(bottom, right, diagonal)
            else:
                cache[(curr_row, curr_col)] = 0

        return cache[(curr_row, curr_col)]

    dfs(0, 0)
    return max(cache.values()) ** 2


# iterative solution (bottom-to-top approach)
def maximal_square_2(matrix):
    rows, columns = len(matrix), len(matrix[0])
    bottom_row = [0] * (columns + 1)
    max_value = 0

    for row in range(rows - 1, -1, -1):
        for column in range(columns - 1, -1, -1):
            if matrix[row][column] == "1":
                # get the min of bottom, right and diagonal values
                bottom = bottom_row[column]
                right = bottom_row[column + 1]
                diagonal = 0 if row + 1 >= rows or column + 1 >= columns else int(matrix[row + 1][column + 1])
                bottom_row[column] = 1 + min(bottom, right, diagonal)
                max_value = max(max_value, bottom_row[column])
                # update the diagonal value in the original matrix
                matrix[row][column] = bottom_row[column]
            else:
                bottom_row[column] = 0

    return max_value ** 2


res = maximal_square_2(
    [["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"],
     ["0", "0", "1", "1", "1"]])
print(res)
