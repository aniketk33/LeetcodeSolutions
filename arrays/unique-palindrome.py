from collections import Counter


def unique_palindrome(s):
    # store the palindrome string .i.e. the middle and outer characters
    result = set()
    left_chars = set()
    right_chars = Counter(s)

    for i in range(len(s)):
        middle_char = s[i]
        # decrement the count
        right_chars[middle_char] -= 1

        # pop if its count is zero
        if right_chars[middle_char] == 0:
            right_chars.pop(middle_char)

        # iterate over the alphabets to find the outer chars
        for j in range(26):
            # get the char based on the ascii value
            outer_char = chr(ord('a') + j)
            if outer_char in left_chars and outer_char in right_chars:
                result.add((middle_char, outer_char))

        # add the middle char to the left chars set
        left_chars.add(middle_char)

    return len(result)


res = unique_palindrome('aabca')
print(res)
