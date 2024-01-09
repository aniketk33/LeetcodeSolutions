def first_missing(nums):
    nums = set(nums)
    result = 1
    for i in range(1, len(nums) + 1):
        if result in nums:
            result += 1
            continue

        return result

    return result


res = first_missing([0, 1, 2])
print(res)
