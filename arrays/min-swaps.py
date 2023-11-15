def min_swaps(s):
    closing_bracket_count, max_count = 0, 0

    for char in s:
        # each time we encounter a ']' bracket, we increment the count
        if char == ']':
            closing_bracket_count += 1
        else:
            closing_bracket_count -= 1
        max_count = max(max_count, closing_bracket_count)

    return (max_count + 1) // 2


res = min_swaps('][')
print(res)
