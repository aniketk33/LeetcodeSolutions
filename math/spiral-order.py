def spiral_order(matrix):
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    order = []

    while left < right and top < bottom:
        # left to right
        for i in range(left, right):
            order.append(matrix[top][i])
        # move the top boundary
        top += 1

        # top to bottom
        for i in range(top, bottom):
            order.append(matrix[i][right - 1])
        # move the right boundary
        right -= 1

        # after the first iteration, all the boundaries were explored, so we need to check for the boundary cases again
        # as we will be traversing them below
        if not (left < right and top < bottom):
            break

        # right to left
        for i in range(right - 1, left - 1, -1):
            order.append(matrix[bottom - 1][i])
        # move the bottom boundary
        bottom -= 1

        # bottom to top
        for i in range(bottom - 1, top - 1, -1):
            order.append(matrix[i][left])
        # move the left boundary
        left += 1

    return order


res = spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(res)
