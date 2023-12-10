def max_subarray(nums):
    curr_sum, max_sum = 0, nums[0]

    for num in nums:
        # if negative sum so far then reset to 0
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(max_sum, curr_sum)

    return max_sum


res = max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)
