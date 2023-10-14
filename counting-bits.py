def count_bits(n):
    result = []
    dp = {}
    for i in range(n + 1):
        count = 0
        while i:
            if i in dp:
                if dp[i]:
                    count += 1
                i = int(i / 2)
                continue
            remainder = i % 2
            if remainder:
                count += 1
            dp[i] = remainder
            i = int(i / 2)
        result.append(count)

    return result


def count_bits_2(n):
    """more efficient dynamic programming solution"""
    # define all the values as 0
    dp = [0] * (n + 1)
    # offset is [1,2,4,8,16..]
    offset = 1
    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp


num = 5
res = count_bits_2(num)
print(res)
