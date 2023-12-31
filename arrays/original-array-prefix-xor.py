def prefix_xor(nums):
    prev_num = nums[0]
    for i in range(1, len(nums)):
        curr_num = nums[i]
        nums[i] = prev_num ^ nums[i]
        prev_num = curr_num

    return nums


res = prefix_xor([5, 2, 0, 3, 1])
print(res)
