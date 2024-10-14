def search(matrix, target):
    for row in matrix:
        # applying binary search for every row
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            if row[mid] > target:
                right -= 1
            else:
                left += 1

    return False


def search_2(matrix, target):
    # starting from the bottom left, move right if greater and move up if smaller
    row = len(matrix) - 1
    col = 0

    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] == target:
            return True
        # move right if the target is greater
        if matrix[row][col] < target:
            col += 1
        else:
            row -= 1

    return False


# res = search([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)
res = search_2([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)
print(res)
