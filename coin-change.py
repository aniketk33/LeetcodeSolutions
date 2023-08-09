"""You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""
from math import inf


def coin_change(coins_arr, amount):
    # memo = {}  # memoization

    def dfs(total_sum, memo):
        if total_sum in memo:
            return memo[total_sum]

        if total_sum == amount:
            return 0

        if total_sum > amount:
            return inf

        coin_count = inf
        for coin in coins_arr:
            ans = dfs(total_sum + coin, memo)  # update amount left state
            if ans == inf:
                continue
            coin_count = min(coin_count, ans + 1)

        memo[total_sum] = coin_count
        return coin_count

    result = dfs(0, {})
    return -1 if result == inf else result


coins = [1, 2, 5]
target = 11
res = coin_change(coins, target)
print(res)
