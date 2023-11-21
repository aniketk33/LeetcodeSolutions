def min_operations(nums, x):
    arr_sum = sum(nums)
    target = arr_sum - x

    left_ptr, right_ptr = 0, 0
    result = len(nums) + 1
    curr_sum = 0

    while right_ptr < len(nums):
        curr_sum += nums[right_ptr]

        # IMP
        # the left pointer may go beyond the right pointer
        while left_ptr <= right_ptr and curr_sum > target:
            curr_sum -= nums[left_ptr]
            left_ptr += 1

        # IMP
        if curr_sum == target:
            # we need remaining_window_size because removing those elements will minimize the result
            # e.g., [1,1,4,2,3] and x=5 if we find the window as [1,1,4] which sums up to 6,
            # then the result is from the last two elements that is the smallest window size and sums up to x
            remaining_window_size = len(nums) - (right_ptr - left_ptr + 1)
            result = min(remaining_window_size, result)

        right_ptr += 1

    return -1 if result == len(nums) + 1 else result


res = min_operations([1, 1, 4, 2, 3], 5)
print(res)
