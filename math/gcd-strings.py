def gcd(str1, str2):
    l1, l2 = len(str1), len(str2)

    def valid_substring(curr_len):
        if l1 % curr_len != 0 or l2 % curr_len != 0:
            return False

        substring_len1, substring_len2 = l1 // curr_len, l2 // curr_len
        # check on the same input string str1
        return str1[:curr_len] * substring_len1 == str1 and str1[:curr_len] * substring_len2 == str2

    for i in range(min(l1, l2), 0, -1):
        if valid_substring(i):
            return str1[:i]

    return ""


res = gcd('ababab', 'abab')
print(res)
