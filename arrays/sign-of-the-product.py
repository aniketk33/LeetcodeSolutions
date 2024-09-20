def sign(nums):
    # if 0 in nums:
    #     return 0
    #
    # product = 1
    # for num in nums:
    #     product *= num
    #
    # return 1 if product > 0 else -1
    # NOTE: Calculating the product is not necessary (Read the problem description).
    # Only calculating the negative numbers will save integer over-overflowing.
    if 0 in nums:
        return 0
    negative_sign = 0
    for num in nums:
        if num > 0:
            continue
        negative_sign += 1
    return 1 if negative_sign % 2 == 0 else -1


# much optimal solution
def sign_2(nums):
    product = 1

    for num in nums:
        if num == 0:
            return 0

        product *= num

    return 1 if product > 0 else -1


res = sign([-1, -2, -3, -4, 3, 2, 1])
print(res)
