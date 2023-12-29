def shuffle(nums, n):
    result = []
    left_ptr, right_ptr = 0, n

    # result.append(nums[0])
    while left_ptr < n and right_ptr < len(nums):
        result.append(nums[left_ptr])
        result.append(nums[right_ptr])
        left_ptr += 1
        right_ptr += 1

    return result


res = shuffle([2, 5, 1, 3, 4, 7], 3)
print(res)
