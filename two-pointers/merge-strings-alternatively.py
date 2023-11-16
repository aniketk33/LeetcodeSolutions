def merge_strings(word1, word2):
    left_ptr, right_ptr = 0, 0
    result = ''

    # both the pointers should be in range
    while left_ptr < len(word1) and right_ptr < len(word2):
        result += word1[left_ptr] + word2[right_ptr]
        left_ptr, right_ptr = left_ptr + 1, right_ptr + 1

    # add remaining chars from either of the words
    while left_ptr < len(word1):
        result += word1[left_ptr]
        left_ptr += 1

    while right_ptr < len(word2):
        result += word2[right_ptr]
        right_ptr += 1

    return result


res = merge_strings('abc', 'pqr')
print(res)
