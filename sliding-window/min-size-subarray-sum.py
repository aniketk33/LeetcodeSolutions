def min_size(nums, target):
    left_ptr, right_ptr = 0, 0
    result = len(nums) + 1
    curr_sum = 0

    while right_ptr < len(nums):
        # add the number to the current sum
        curr_sum += nums[right_ptr]

        # check if it is greater/equal than target and keep incrementing the left_ptr
        while curr_sum >= target:
            # calculate the window size
            result = min((right_ptr - left_ptr + 1), result)
            curr_sum -= nums[left_ptr]
            left_ptr += 1

        right_ptr += 1

    return 0 if result == len(nums) + 1 else result


res = min_size([2, 3, 1, 2, 4, 3], 7)
print(res)
