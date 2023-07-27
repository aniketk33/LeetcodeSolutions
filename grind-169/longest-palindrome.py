"""Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome
that can be built with those letters.

Letters are case-sensitive, for example, "Aa" is not considered a palindrome here.

"""


def longest_palindrome(s):
    chars = set()
    result = 0
    for c in s:
        if c in chars:
            result += 2
            chars.remove(c)
        else:
            chars.add(c)

    return result + 1 if len(chars) > 0 else result


input_str = "abccccdd"
res = longest_palindrome(input_str)
print(res)
