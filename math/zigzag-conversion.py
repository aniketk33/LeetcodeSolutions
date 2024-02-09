def zigzag(s, rows):
    if rows == 1:
        return s

    result = ''
    for r in range(rows):
        increment = (rows - 1) * 2
        # starting from the current row
        for i in range(r, len(s), increment):
            # for the first and last row
            result += s[i]

            # for between rows
            if 0 < r < rows - 1 and (i + increment - 2 * r) < len(s):
                result += s[i + increment - 2 * r]

    return result


res = zigzag('PAYPALISHIRING', 3)
print(res)
