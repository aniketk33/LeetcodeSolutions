def int_roman(num):
    symbols = [
        ["I", 1],
        ["IV", 4],
        ["V", 5],
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000],
    ]

    result = ''

    # start from the greatest pair
    for sym, val in reversed(symbols):
        if num // val == 0:
            continue

        count = num // val
        result += (sym * count)
        num = num % val

    return result


res = int_roman(8)
print(res)
