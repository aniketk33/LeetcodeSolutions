def disappeared_nums(nums):
    # result = []
    # n = len(nums)
    #
    # for i in range(1, n + 1):
    #     if i in nums:
    #         continue
    #     result.append(i)
    #
    # return result

    # optimal solution

    # mark the values as -1
    for num in nums:
        idx = abs(num) - 1
        nums[idx] = -1 * abs(num)

    result = []
    for idx, num in enumerate(nums):
        if num > 0:
            result.append(idx + 1)

    return result


res = disappeared_nums([4, 3, 2, 7, 8, 2, 3, 1])
print(res)
