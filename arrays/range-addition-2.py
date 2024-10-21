def range_addition(m, n, ops):
    # create a matrix with zeros
    matrix = [[0] * n for _ in range(m)]

    max_val = 0

    # perform the increment operations and keep track of max value
    for op in ops:
        total_row, total_col = op
        for r in range(total_row):
            for c in range(total_col):
                matrix[r][c] += 1
                # keep track of the max val
                if matrix[r][c] > max_val:
                    max_val = matrix[r][c]

    count = 0
    for row in matrix:
        # count += row.count(max_val)
        for val in row:
            count += 1 if val == max_val else 0

    return count


# optimal solution O(1) space
def range_addition_2(m, n, ops):
    # calculate the overlapping row and col
    min_row = m
    min_col = n

    for row, col in ops:
        # row, col = op
        # get the overlapping value i.e., the min val between the given and current row/col
        if min_row > row:
            min_row = row
        if min_col > col:
            min_col = col

    return min_row * min_col


# res = range_addition(3, 3,
#                      [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]])
# res = range_addition(10**4, 10**4, [])
res = range_addition_2(10**4, 10**4, [])
print(res)
