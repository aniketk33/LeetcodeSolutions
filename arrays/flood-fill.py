def flood_fill(image, sr, sc, color):
    """sr and sc are the starting position in 2D array"""
    need_to_visit = set()
    # add the initial positions
    need_to_visit.add((sr, sc))

    visited = set()

    rows, cols = len(image), len(image[0])

    while need_to_visit:
        row, col = need_to_visit.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        # check all the adjacent places
        # above row and same column
        if row - 1 >= 0 and image[row - 1][col] == image[row][col]:
            need_to_visit.add((row - 1, col))
        # same row and right column
        if col + 1 < cols and image[row][col + 1] == image[row][col]:
            need_to_visit.add((row, col + 1))
        # below row and same column
        if row + 1 < rows and image[row + 1][col] == image[row][col]:
            need_to_visit.add((row + 1, col))
        # same row and left column
        if col - 1 >= 0 and image[row][col - 1] == image[row][col]:
            need_to_visit.add((row, col - 1))

        # replace the old color with the new color
        image[row][col] = color

    return image


res = flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
print(res)
