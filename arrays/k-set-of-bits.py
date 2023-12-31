def k_set(nums, k):
    result = 0
    for idx in range(len(nums)):
        binary = bin(idx)
        curr_count = binary.count('1')
        if curr_count == k:
            result += nums[idx]

    return result


res = k_set([5, 10, 1, 5, 2], 1)
print(res)
