def delete_columns(strs):
    rows = len(strs)
    columns = len(strs[0])
    count = 0

    for c in range(columns):
        r = 0
        # break if it is not in the ascending order
        while r < rows - 1 and strs[r][c] <= strs[r + 1][c]:
            r += 1
        if r != rows - 1:
            count += 1

    return count


res = delete_columns(["zyx", "wvu", "tsr"])
print(res)
