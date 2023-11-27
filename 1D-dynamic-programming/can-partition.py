def can_partition(nums):
    # if the sum is odd, then return false
    if sum(nums) % 2:
        return False
    target = sum(nums) // 2
    cache = set()
    cache.add(0)

    for i in range(len(nums) - 1, -1, -1):
        curr_cache = set()
        for num in cache:
            curr_sum = nums[i] + num
            if target == curr_sum:
                return True
            curr_cache.add(curr_sum)
            curr_cache.add(num)
        cache = curr_cache

    return False


res = can_partition([1, 5, 11, 5])
print(res)
