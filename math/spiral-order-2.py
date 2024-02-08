def spiral_order(n):
    left, right = 0, n
    top, bottom = 0, n
    order = [[0] * n for _ in range(n)]
    val = 1

    while left < right and top < bottom:
        # left to right
        for i in range(left, right):
            order[left][i] = val
            val += 1
        # move the top boundary
        top += 1

        # top to bottom
        for i in range(top, bottom):
            order[i][right - 1] = val
            val += 1
        # move the right boundary
        right -= 1

        # after the first iteration, all the boundaries were explored, so we need to check for the boundary cases again
        # as we will be traversing them below
        if not (left < right and top < bottom):
            break

        # right to left
        for i in range(right - 1, left - 1, -1):
            # the row same and column will change
            order[bottom - 1][i] = val
            val += 1
        # move the bottom boundary
        bottom -= 1

        # bottom to top
        for i in range(bottom - 1, top - 1, -1):
            # keep the column same and the row val will change
            order[i][left] = val
            val += 1
        # move the left boundary
        left += 1

    return order


res = spiral_order(3)
print(res)
