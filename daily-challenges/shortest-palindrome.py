# this solution does not pass this test case 'aabba'. need a re-work on this solution.
# I had guessed it on my first attempt
def shortest_palindrome(s):
    missing_chars = ''
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
        else:
            missing_chars += s[right]
        right -= 1

    return missing_chars + s


def shortest_palindrome_2(s: str):
    reverse = s[::-1]

    # get the starting of the original string from the reversed string
    for i in range(len(s)):
        if s.startswith(reverse[i:]):
            return reverse[:i] + s

    return reverse + s


# res = shortest_palindrome('aabba')
res = shortest_palindrome_2('aabba')
print(res)
