def num_lines(widths, s):
    i = 0
    pixel_length = 0
    line_count = 0

    while i < len(s):
        curr_length = 0
        while i < len(s) and curr_length + widths[ord(s[i]) - ord('a')] <= 100:
            loc = ord(s[i]) - ord('a')
            curr_length += widths[loc]
            i += 1
        line_count += 1
        pixel_length = curr_length

    return [line_count, pixel_length]


# use of single loop
def num_lines_2(widths, s):
    pixel_length = 0
    line_count = 1

    for c in s:
        loc = ord(c) - ord('a')
        if pixel_length + widths[loc] > 100:
            line_count += 1
            # store tha last char width
            pixel_length = widths[loc]
        else:
            pixel_length += widths[loc]

    return [line_count, pixel_length]


w = [3, 4, 10, 4, 8, 7, 3, 3, 4, 9, 8, 2, 9, 6, 2, 8, 4, 9, 9, 10, 2, 4, 9, 10, 8, 2]

# res = num_lines(w, 'mqblbtpvicqhbrejb')
res = num_lines_2(w, 'mqblbtpvicqhbrejb')
print(res)
