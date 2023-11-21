def max_frequency(nums, k):
    nums.sort()
    left_ptr, right_ptr = 0, 0
    result = 0
    curr_window_sum = 0

    while right_ptr < len(nums):
        curr_window_sum += nums[right_ptr]

        # using the formula:
        # curr_num * (window length) <= curr_window_sum + k
        while nums[right_ptr] * (right_ptr - left_ptr + 1) > curr_window_sum + k:
            curr_window_sum -= nums[left_ptr]
            left_ptr += 1

        # get the max of previous and current window length
        result = max(result, (right_ptr - left_ptr + 1))
        right_ptr += 1

    return result


res = max_frequency([3, 9, 6], 2)
print(res)
