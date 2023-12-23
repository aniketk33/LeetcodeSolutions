def find_anagrams(s, p):
    if len(p) > len(s):
        return []
    s_count, p_count = {}, {}

    for i in range(len(p)):
        p_count[p[i]] = 1 + p_count.get(p[i], 0)
        # initialize the s dict too
        s_count[s[i]] = 1 + s_count.get(s[i], 0)

    # check if the above dict is the same
    if s_count == p_count:
        # add the first index to the result
        result = [0]
    else:
        result = []

    left_ptr, right_ptr = 0, len(p)
    while right_ptr < len(s):
        # add the right element
        s_count[s[right_ptr]] = 1 + s_count.get(s[right_ptr], 0)
        # remove the left element
        s_count[s[left_ptr]] -= 1
        # remove the element whose count is 0
        if s_count[s[left_ptr]] == 0:
            s_count.pop(s[left_ptr])
        left_ptr += 1
        right_ptr += 1
        # check if they are the same
        if s_count == p_count:
            result.append(left_ptr)

    return result


res = find_anagrams('cbaebabacd', 'abc')
print(res)
