def perfect_sq(n):
    # we to need to find the min so storing the max value
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for target in range(1, n + 1):
        for i in range(1, target + 1):
            square = i ** 2
            # move onto the next number
            if target - square < 0:
                break

            dp[target] = min(dp[target], 1 + dp[target - square])

    return dp[n]


res = perfect_sq(12)
print(res)
