def excel_sheet(column_num):
    result = ''

    while column_num > 0:
        # first mod
        remainder = (column_num - 1) % 26
        result += chr(ord('A') + remainder)
        # then divide
        column_num = (column_num - 1) // 26

    return result[::-1]


res = excel_sheet(52)
print(res)
