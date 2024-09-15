from collections import Counter


# with extra space
def set_mismatch(nums):
    # duplicate, missing value
    result = [0, 0]
    count = Counter(nums)

    for i in range(1, len(nums) + 1):
        # missing value
        if count[i] == 0:
            result[1] = i
        # duplicate value
        if count[i] == 2:
            result[0] = i

    return result


# with equations
def set_mismatch_2(nums):
    # solving using two equations
    # 1) D - M = x
    x = 0
    # 2) D^2 - M^2 = y
    y = 0

    for i in range(1, len(nums) + 1):
        x += nums[i - 1] - i
        y += nums[i - 1] ** 2 - i ** 2

    # solving for duplicate and missing value
    # D = (x ** 2 + y) // (2 * x)
    M = (y - x ** 2) // (2 * x)
    D = x + M
    return [D, M]


# res = set_mismatch([2, 2])
res = set_mismatch_2([2, 2])
print(res)
