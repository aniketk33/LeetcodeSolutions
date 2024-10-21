def reshape(mat, r, c):
    rows = len(mat)
    cols = len(mat[0])

    if rows * cols != r * c:
        return mat

    # flatten the given matrix
    # flatten = [mat[i][j] for i in range(rows) for j in range(cols)]
    flatten = []
    for m in mat:
        flatten += m

    result = []
    for curr_row in range(r):
        # at a given row, take these many 'c(total col)' values
        row = flatten[curr_row * c: curr_row * c + c]
        result.append(row)

    return result


res = reshape([[1, 2], [3, 4]], 1, 4)
print(res)
