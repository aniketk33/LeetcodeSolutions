def target_sum(nums, target):
    cache = {}

    def dfs(curr_idx, curr_sum):
        if curr_idx >= len(nums):
            return 1 if curr_sum == target else 0

        if (curr_idx, curr_sum) in cache:
            return cache[(curr_idx, curr_sum)]

        # either add the curr num or subtract
        cache[(curr_idx, curr_sum)] = dfs(curr_idx + 1, curr_sum + nums[curr_idx]) + dfs(curr_idx + 1,
                                                                                         curr_sum - nums[curr_idx])

        return cache[(curr_idx, curr_sum)]

    return dfs(0, 0)


res = target_sum([1, 1, 1, 1, 1], 3)
print(res)
