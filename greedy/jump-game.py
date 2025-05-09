def can_jump(nums):
    # last index
    target = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        # check if the previous val can make it to the target
        if i + nums[i] >= target:
            # shift the current pointer as the new target
            target = i

    return target == 0


def can_jump_2(nums):
    gas = 0

    for curr_gas in nums:
        # if we ran out of gas
        if gas < 0:
            return False
        # refuel the gas with higher value
        if curr_gas > gas:
            gas = curr_gas
        # decrease the gas by one at every iteration
        gas -= 1

    return True


# res = can_jump([2, 3, 1, 1, 4])
res = can_jump_2([2, 3, 1, 1, 4])
print(res)
