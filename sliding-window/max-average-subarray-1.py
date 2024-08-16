def max_avg_subarray(nums, k):
    max_avg = float('-inf')
    left, right = 0, k
    curr_avg = sum(nums[left: right])
    max_avg = max(max_avg, curr_avg)

    while right < len(nums):
        curr_avg -= nums[left]
        curr_avg += nums[right]
        max_avg = max(max_avg, curr_avg)
        left += 1
        right += 1

    return max_avg / k


# res = max_avg_subarray([1, 12, -5, -6, 50, 3], 4)
res = max_avg_subarray([0, 4, 0, 3, 2], 1)
print(res)
