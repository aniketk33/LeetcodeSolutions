def rotate_image(matrix):
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # store top left in the temp variable
            top_left = matrix[top][left + i]
            # performing reverse rotation
            # move bottom left to the top left corner
            matrix[top][left + i] = matrix[bottom - i][left]
            # move bottom right to the bottom left corner
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # move top right to the bottom right corner
            matrix[bottom][right - i] = matrix[top + i][right]
            # move the top left to the top right
            matrix[top + i][right] = top_left

        right -= 1
        left += 1


image = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(image)
rotate_image(image)
print(image)
