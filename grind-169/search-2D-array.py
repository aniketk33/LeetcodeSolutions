"""You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity."""


def search_matrix(num_arr, target):
    i, j = 0, len(num_arr[0]) - 1
    while 0 <= i < len(num_arr) and 0 <= j < len(num_arr[0]):
        if num_arr[i][j] == target:
            return True
        if num_arr[i][j] > target:
            j -= 1
        else:
            i += 1

    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
res = search_matrix(matrix, target)
print(res)
