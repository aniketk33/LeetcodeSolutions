def can_jump(nums):
    # last index
    target = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        # check if the previous val can make it to the target
        if i + nums[i] >= target:
            # shift the current pointer as the new target
            target = i

    return target == 0


res = can_jump([2, 3, 1, 1, 4])
print(res)
