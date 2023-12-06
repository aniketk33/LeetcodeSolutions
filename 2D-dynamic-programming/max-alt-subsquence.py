# using recursion
def max_subsquence(nums):
    cache = {}

    def dfs(curr_idx, is_even):
        if curr_idx >= len(nums):
            return 0
        if (curr_idx, is_even) in cache:
            return cache[(curr_idx, is_even)]

        # check if it is even then subtract with total
        curr_total = nums[curr_idx] if is_even else (-1 * nums[curr_idx])
        # two choices: either add the value or skip
        cache[(curr_idx, is_even)] = max(curr_total + dfs(curr_idx + 1, not is_even), dfs(curr_idx + 1, is_even))

        return cache[(curr_idx, is_even)]

    return dfs(0, True)


# using dynamic programming
def max_subsquence_2(nums):
    curr_sum_odd, curr_sum_even = 0, 0
    for i in range(len(nums) - 1, -1, -1):
        # moving from odd to even
        temp_even_sum = max(curr_sum_odd + nums[i], curr_sum_even)
        # moving from even to odd
        temp_odd_sum = max(curr_sum_even - nums[i], curr_sum_odd)
        curr_sum_even, curr_sum_odd = temp_even_sum, temp_odd_sum

    return curr_sum_even


res = max_subsquence_2([4, 2, 5, 3])
print(res)
