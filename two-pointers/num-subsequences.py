def num_subsequences(nums, target):
    nums.sort()
    result = 0
    mod = 10 ** 9 + 7
    right_ptr = len(nums) - 1

    for left_ptr, val in enumerate(nums):
        # get the subsequences which are less than target
        while val + nums[right_ptr] > target and left_ptr <= right_ptr:
            right_ptr -= 1

        # add to the result using the formula 2^(right_index - left_index)
        if left_ptr <= right_ptr:
            result += 2 ** (right_ptr - left_ptr)
            result %= mod

    return result


res = num_subsequences([2, 3, 3, 4, 6, 7], 12)
print(res)
