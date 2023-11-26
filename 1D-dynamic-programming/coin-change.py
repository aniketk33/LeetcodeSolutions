"""You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.

Return the lowest number of coins that you need to make up that amount.
If that amount of money cannot be made up by
any combination of the coins, return -1.

You may assume that you have an infinite amount of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""
from math import inf


def coin_change(coins_arr, amount):
    memo = {}  # memoization

    def dfs(total_sum):
        if total_sum in memo:
            return memo[total_sum]

        if total_sum == amount:
            return 0

        if total_sum > amount:
            return inf

        coin_count = inf
        for coin in coins_arr:
            ans = dfs(total_sum + coin)  # update amount left state
            if ans == inf:
                continue
            coin_count = min(coin_count, ans + 1)

        memo[total_sum] = coin_count
        return coin_count

    result = dfs(0)
    return -1 if result == inf else result


# without using dfs
def coin_change_2(coin_arr, target):
    cache = [target + 1] * (target + 1)
    # for amount 0, 0 coins will be required
    cache[0] = 0
    # get coins for every amount up to target
    for amount in range(1, target + 1):
        for coin in coin_arr:
            # the difference should be greater than zero
            if amount - coin >= 0:
                # coin equation break-up: 1(for given amount) + coin required for remaining amount
                cache[amount] = min(cache[amount], 1 + cache[amount - coin])

    return cache[target] if cache[target] != target + 1 else -1


coins = [1, 3, 4, 5]
tar = 7
res = coin_change_2(coins, tar)
print(res)
