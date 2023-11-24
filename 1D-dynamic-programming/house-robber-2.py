def house_robber_1(nums):
    left, right = 0, 0
    for num in nums:
        curr = max(left + num, right)
        left = right
        right = curr

    return right


def house_robber_2(nums):
    # include first and exclude last
    first_half = house_robber_1(nums[:-1])
    # exclude first and include last
    second_half = house_robber_1(nums[1:])
    # edge case: if there was only a single element present, then it will return zero so including the single element in
    # the max function
    return max(first_half, second_half, nums[0])


res = house_robber_2([2, 3, 2])
print(res)
