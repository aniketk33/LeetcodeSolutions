def longest_subsquence(nums):
    cache = [1] * len(nums)

    for curr_idx in range(len(nums) - 1, -1, -1):
        # calculate from the next element
        for j in range(curr_idx + 1, len(nums)):
            if nums[j] > nums[curr_idx]:
                cache[curr_idx] = max(cache[curr_idx], 1 + cache[j])

    return max(cache)


res = longest_subsquence([1, 2, 4, 3])
print(res)
