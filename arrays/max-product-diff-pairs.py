def max_product(nums):
    nums.sort(reverse=True)

    a, b, c, d = nums[0], nums[1], nums[-2], nums[-1]

    return (a * b) - (c * d)


res = max_product([5, 6, 2, 7, 4])
print(res)
