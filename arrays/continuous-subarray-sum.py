def continuous_sum(nums, k):
    total = 0
    result = {0: -1}

    for idx, num in enumerate(nums):
        total += num
        remainder = total % k
        if remainder not in result:
            result[remainder] = idx
        elif idx - result[remainder] >= 2:
            return True

    return False


res = continuous_sum([23, 2, 6, 4, 7], 13)
print(res)
