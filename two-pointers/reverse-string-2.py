def reverse_string(s, k):
    # to prevent the out of bound condition, we take the min value for the right pointer
    left, right = 0, min(k, len(s))

    while left < len(s):
        # add the chars up to the left, then reverse until the right position and add the remaining
        s = s[:left] + s[left:right][::-1] + s[right:]

        left += 2 * k
        right = min(left + k, len(s))

    return s


res = reverse_string('abcdefg', 2)
print(res)
