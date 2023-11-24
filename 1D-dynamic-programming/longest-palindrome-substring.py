def longest_substring(s):
    max_len = 0
    result = ''

    for i in range(len(s)):
        # for odd length string
        left_ptr, right_ptr = i, i
        # check for out of bounds and palindrome case
        while left_ptr >= 0 and right_ptr < len(s) and s[left_ptr] == s[right_ptr]:
            if (right_ptr - left_ptr + 1) > max_len:
                result = s[left_ptr:right_ptr + 1]
                max_len = right_ptr - left_ptr + 1
                # move towards the left
            left_ptr -= 1
            # move towards the right
            right_ptr += 1

        # even length string
        left_ptr, right_ptr = i, i + 1
        while left_ptr >= 0 and right_ptr < len(s) and s[left_ptr] == s[right_ptr]:
            if (right_ptr - left_ptr + 1) > max_len:
                result = s[left_ptr:right_ptr + 1]
                max_len = right_ptr - left_ptr + 1
                # move towards the left
            left_ptr -= 1
            # move towards the right
            right_ptr += 1

    return result


res = longest_substring("babad")
print(res)
