def min_jumps(nums):
    left_ptr = right_ptr = 0
    jumps = 0

    while right_ptr < len(nums) - 1:
        jump_value = 0
        for i in range(left_ptr, right_ptr + 1):
            # get the max jump within the range
            jump_value = max(jump_value, i + nums[i])
        left_ptr = right_ptr + 1
        right_ptr = jump_value
        jumps += 1

    return jumps


res = min_jumps([2, 3, 1, 1, 4])
print(res)
