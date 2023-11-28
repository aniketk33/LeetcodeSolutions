def buy_sell_stock(nums):
    # store index and is_buying state
    cache = {}

    # state: buying or selling
    # buying: move by 1
    # selling: move by 2 as we cannot buy the next day, we need a cooldown period

    def dfs(curr_idx, buying):
        if curr_idx >= len(nums):
            return 0

        if (curr_idx, buying) in cache:
            return cache[(curr_idx, buying)]

        if buying:
            # tell the next state that we already bought the share and pass False
            buy = dfs(curr_idx + 1, False) - nums[curr_idx]
            cooldown = dfs(curr_idx + 1, buying)
            cache[(curr_idx, True)] = max(buy, cooldown)
        # selling
        else:
            # tell the next state that you can buy the stock
            sell = dfs(curr_idx + 2, True) + nums[curr_idx]
            cooldown = dfs(curr_idx + 1, buying)
            cache[(curr_idx, False)] = max(sell, cooldown)

        return cache[(curr_idx, buying)]

    # always buy at index 1
    return dfs(0, True)


res = buy_sell_stock([1, 2, 3, 0, 2])
print(res)
