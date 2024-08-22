def min_swaps(nums):
    total = 0
    for n in nums:
        if n == 1:
            total += 1

    curr_window = 0
    for right in range(total):
        curr_window += nums[right]

    swaps = total - curr_window

    for right in range(total, len(nums)):
        curr_window += nums[right]
        curr_window -= nums[right - total]
        swaps = min(swaps, total - curr_window)

    return swaps


res = min_swaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1])
print(res)
