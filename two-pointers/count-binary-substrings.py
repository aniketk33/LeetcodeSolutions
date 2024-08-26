def count_binary(s):
    count = prev_len = 0
    curr_len = 1
    prev_char = s[0]

    for curr_char in s[1:]:
        # keep increasing the current length if they are the same
        if curr_char == prev_char:
            curr_len += 1
        else:
            count += min(prev_len, curr_len)
            prev_len = curr_len
            curr_len = 1
            prev_char = curr_char

    # add the count for the last window
    count += min(prev_len, curr_len)

    return count


res = count_binary('00110011')
print(res)
