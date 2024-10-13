def pascals_triangle(n):
    result = [[1]]

    for i in range(n - 1):
        # add zeros at the beginning and end for adding start and end value
        curr_row = [0] + result[-1] + [0]
        curr_result = []
        # iterate over the current row
        for j in range(len(curr_row) - 1):
            curr_val = curr_row[j] + curr_row[j + 1]
            curr_result.append(curr_val)

        result.append(curr_result)

    return result


def pascals_triangle_2(n):
    triangle = []

    for row in range(n):
        curr_row = [1] * (row + 1)
        # we need to iterate from the 1st column
        for col in range(1, row):
            # current column's value is [prev_row][curr_col-1] + [prev_row][curr_col]
            curr_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
        triangle.append(curr_row)

    return triangle


# res = pascals_triangle(5)
res = pascals_triangle_2(5)
print(res)
