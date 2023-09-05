"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
"""


def is_subsequence(s, t):
    if s == '':
        return True
    left_ptr, i = 0, 0
    while left_ptr < len(t) and i < len(s):
        if t[left_ptr] == s[i]:
            left_ptr += 1
            i += 1
            continue
        left_ptr += 1

    return i == len(s)


s = "b"
t = "ahbgdc"
res = is_subsequence(s, t)
print(res)
