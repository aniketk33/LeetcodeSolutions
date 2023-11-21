def min_flips(s):
    str_len = len(s)
    # add the string to itself
    s += s
    # create two strings of alternating zeros and ones
    alt_str1, alt_str2 = '', ''
    for i in range(len(s)):
        alt_str1 += '0' if i % 2 == 0 else '1'
        alt_str2 += '1' if i % 2 == 0 else '0'

    left_ptr, right_ptr = 0, 0
    diff1, diff2 = 0, 0
    result = len(s)

    while right_ptr < len(s):
        # count the differences for both the created strings
        if s[right_ptr] != alt_str1[right_ptr]:
            diff1 += 1
        if s[right_ptr] != alt_str2[right_ptr]:
            diff2 += 1

        if (right_ptr - left_ptr + 1) > str_len:
            if s[left_ptr] != alt_str1[left_ptr]:
                diff1 -= 1
            if s[left_ptr] != alt_str2[left_ptr]:
                diff2 -= 1
            left_ptr += 1

        # calculate only when the window size is equal to the given string size
        if (right_ptr - left_ptr + 1) == str_len:
            result = min(diff1, diff2, result)
        right_ptr += 1

    return result


res = min_flips('111000')
print(res)
