def longest_sequence(s):
    left, right = 0, 0
    curr_window = ''
    longest = 0

    while right < len(s):
        if s[right] in curr_window:
            while s[left] != s[right]:
                left += 1
            left += 1
        longest = max(longest, right - left + 1)
        right += 1
        curr_window = s[left:right]

    return longest


# brute force (does not work for longer input)
def longest_sequence_2(s):
    arr_len = len(s)
    longest = 0
    for left in range(arr_len):
        for right in range(arr_len):
            curr_window = s[left:right + 1]
            if len(set(curr_window)) == len(curr_window):
                longest = max(longest, right - left + 1)
            else:
                break

    return longest


# optimal solution
def longest_sequence_3(s):
    arr_len = len(s)
    left, right = 0, 0
    result = 0
    # takes O(1) for lookup/delete/insert
    curr_window = set()

    while right < arr_len:
        if s[right] in curr_window:
            while curr_window and s[left] != s[right]:
                curr_window.remove(s[left])
                left += 1
            left += 1
        result = max(result, right - left + 1)
        curr_window.add(s[right])
        right += 1

    return result


# res = longest_sequence_2('abccabcabcc')
res = longest_sequence_3('abccabcabcc')
# res = longest_sequence('aaaabaaa')
print(res)
