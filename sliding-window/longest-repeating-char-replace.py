def replace_char(s, k):
    char_count_dict = {}
    left_ptr, right_ptr = 0, 0
    result = 0
    max_frequency = 0

    while right_ptr < len(s):
        curr_char = s[right_ptr]
        char_count_dict[curr_char] = 1 + char_count_dict.get(curr_char, 0)
        # get the max frequency compared with the recent updated char count
        max_frequency = max(max_frequency, char_count_dict[curr_char])
        # if diff is greater than the threshold, then keep moving the left pointer and update the count
        # get the difference using window length - frequent char count
        while (right_ptr - left_ptr + 1) - max_frequency > k:
            char_count_dict[s[left_ptr]] -= 1
            left_ptr += 1
        # update the result which is the window_len
        result = max(result, right_ptr - left_ptr + 1)

        right_ptr += 1

    return result


res = replace_char("AABABBA", 1)
print(res)
