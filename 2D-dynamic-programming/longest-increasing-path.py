def longest_path(matrix):
    rows, columns = len(matrix), len(matrix[0])
    cache = {}

    def dfs(curr_row, curr_col, prev_val):
        if (curr_row < 0 or curr_row == rows or curr_col < 0 or
                curr_col == columns or matrix[curr_row][curr_col] <= prev_val):
            return 0
        if (curr_row, curr_col) in cache:
            return cache[(curr_row, curr_col)]

        curr_result = 1
        # run dfs on all four positions from the current position and store the max value returned from each position
        # as the current value
        curr_value = matrix[curr_row][curr_col]
        curr_result = max(curr_result, 1 + dfs(curr_row, curr_col + 1, curr_value))
        curr_result = max(curr_result, 1 + dfs(curr_row, curr_col - 1, curr_value))
        curr_result = max(curr_result, 1 + dfs(curr_row + 1, curr_col, curr_value))
        curr_result = max(curr_result, 1 + dfs(curr_row - 1, curr_col, curr_value))

        cache[(curr_row, curr_col)] = curr_result
        return curr_result

    max_path = float('-inf')
    for r in range(rows):
        for c in range(columns):
            # passing -1 as the previous value because all the values will be positive
            max_path = max(max_path, dfs(r, c, -1))

    return max_path


res = longest_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]])
print(res)
