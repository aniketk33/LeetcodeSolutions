def smallest_range(nums, k):
    # minimize the highest value and maximize the lowest value
    return max(0, max(nums) - k - (min(nums) + k))


def smallest_range_2(nums, k):
    result = max(nums) - k - (min(nums) + k)
    return 0 if result < 0 else result


res = smallest_range([1, 3, 6], 3)
print(res)
