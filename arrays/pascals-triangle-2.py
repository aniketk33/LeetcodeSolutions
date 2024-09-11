def pascals(row_index):
    curr_row = [1]

    for row in range(row_index):
        # the next row will be prev_row + 1
        next_row = [0] * (len(curr_row) + 1)
        # iterate over the current row
        for i in range(len(curr_row)):
            next_row[i] += curr_row[i]
            next_row[i + 1] += curr_row[i]
        curr_row = next_row

    return curr_row


def pascals_2(row_index):
    curr_row = [1]
    prev_val = 1

    for i in range(1, row_index + 1):
        next_val = prev_val * (row_index - i + 1) // i
        curr_row.append(next_val)
        prev_val = next_val

    return curr_row


def pascals_3(row_index):
    curr_row = [1]

    for row in range(1, row_index + 1):
        # we need to change the previous row values
        # starting from the previous row last position
        for i in range(row - 1, 0, -1):
            curr_row[i] += curr_row[i - 1]

        curr_row.append(1)

    return curr_row


# res = pascals(4)
# res = pascals_2(3)
res = pascals_3(3)
print(res)
