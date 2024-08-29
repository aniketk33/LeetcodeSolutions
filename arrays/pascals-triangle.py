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


res = pascals_triangle(5)
print(res)
