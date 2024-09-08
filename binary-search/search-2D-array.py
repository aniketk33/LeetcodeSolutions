"""You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity."""


def search_matrix(num_arr, target):
    row, col = 0, len(num_arr[0]) - 1
    while 0 <= row < len(num_arr) and 0 <= col < len(num_arr[0]):
        if num_arr[row][col] == target:
            return True
        if num_arr[row][col] > target:
            col -= 1
        else:
            row += 1

    return False


def search_matrix_2(matrix, target):
    # define row and column variables
    row_top, row_bot = 0, len(matrix) - 1
    col_left, col_right = 0, len(matrix[0]) - 1
    mid_row = 0

    # get the mid-row index
    while row_top <= row_bot:
        mid_row = row_top + (row_bot - row_top) // 2
        if matrix[mid_row][0] == target or matrix[mid_row][-1] == target:
            return True
        # if the target is present above the mid-row
        if matrix[mid_row][0] > target:
            row_bot = mid_row - 1
        # if below the mid-row
        elif matrix[mid_row][-1] < target:
            row_top = mid_row + 1
        # if it is in the mid-row:
        else:
            break

    # get the mid-column
    while col_left <= col_right:
        mid_col = col_left + (col_right - col_left) // 2

        if matrix[mid_row][mid_col] == target:
            return True
        if matrix[mid_row][mid_col] > target:
            col_right = mid_col - 1
        else:
            col_left = mid_col + 1

    return False


# res = search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
res = search_matrix_2([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
print(res)
