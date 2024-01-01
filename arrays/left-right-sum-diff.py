def left_right_sum_diff(nums):
    prefix_arr = [0] * len(nums)
    postfix_arr = [0] * len(nums)
    result = [0] * len(nums)
    prefix, postfix = 0, 0
    # fill the prefix array
    for i in range(1, len(nums)):
        prefix += nums[i - 1]
        prefix_arr[i] += prefix

    # fill the postfix array
    for i in range(len(nums) - 2, -1, -1):
        postfix += nums[i + 1]
        postfix_arr[i] += postfix

    for i in range(len(nums)):
        result[i] = abs(prefix_arr[i] - postfix_arr[i])

    return result


res = left_right_sum_diff([10, 4, 8, 3])
print(res)
