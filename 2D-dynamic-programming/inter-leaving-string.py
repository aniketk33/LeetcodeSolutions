def is_interleaving(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    cache = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    # set the last row and last column value as True
    cache[len(s1)][len(s2)] = True

    for row in range(len(s1), -1, -1):
        for column in range(len(s2), -1, -1):
            # check if it is bound, and it is equal to the char in s3, and the bottom position is True
            if row < len(s1) and s1[row] == s3[row + column] and cache[row + 1][column]:
                cache[row][column] = True
            if column < len(s2) and s2[column] == s3[row + column] and cache[row][column + 1]:
                cache[row][column] = True

    return cache[0][0]


res = is_interleaving('aabcc', 'dbbca', 'aadbbcbcac')
print(res)
