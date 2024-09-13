def max_score(s: str):
    result = 0

    for right in range(1, len(s)):
        zeros = s[:right].count('0')
        ones = s[right:].count('1')
        if zeros + ones > result:
            result = zeros + ones

    return result


# optimal solution
def max_score_2(s):
    ones = zeros = 0
    result = 0
    for c in s:
        if c == '1':
            ones += 1

    for i in range(len(s) - 1):
        if s[i] == '1':
            ones -= 1
        else:
            zeros += 1
        if ones + zeros > result:
            result = ones + zeros

    return result


# res = max_score('011101')
res = max_score_2('00111')
print(res)
