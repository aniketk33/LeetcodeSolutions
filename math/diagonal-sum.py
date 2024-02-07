def diagonal_sum(matrix):
    total_sum = 0
    row, col = 0, 0
    visited = set()
    # primary diagonal
    while row < len(matrix) and col < len(matrix[0]):
        if (row, col) not in visited:
            total_sum += matrix[row][col]
        visited.add((row, col))
        row += 1
        col += 1

    # secondary diagonal
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if (row, col) not in visited:
            total_sum += matrix[row][col]
        visited.add((row, col))
        row += 1
        col -= 1

    return total_sum


res = diagonal_sum([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print(res)
