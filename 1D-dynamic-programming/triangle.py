def min_path(triangle):
    result = 0
    last_row = [0] * (len(triangle[-1]) + 1)

    for i in range(len(triangle) - 1, -1, -1):
        curr_idx = 0
        min_val = float('inf')
        while curr_idx < len(triangle[i]):
            first, second = triangle[i][curr_idx] + last_row[curr_idx], triangle[i][curr_idx] + last_row[curr_idx + 1]
            # get the minimum of addition of current num and below two
            last_row[curr_idx] = min(first, second)
            min_val = min(min_val, first, second)
            curr_idx += 1

        result = min_val

    return result


res = min_path([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
# res = min_path([[-1], [2, 3], [1, -1, -3]])
print(res)
