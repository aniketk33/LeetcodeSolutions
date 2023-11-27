def unique_paths(row, column):
    # starting from the last row, it will be all 1's
    prev_row = [1] * column

    for r in range(row - 1):
        curr_row = [1] * column
        # ignoring the last column as it is also all 1's
        # starting from the second last column
        for c in range(column - 2, -1, -1):
            # current value = right_value of same row + down_value of below row
            curr_row[c] = curr_row[c + 1] + prev_row[c]
        prev_row = curr_row

    return prev_row[0]


res = unique_paths(3, 7)
print(res)
