def house_robber(nums):
    # get the first two values
    left, right = 0, 0
    for num in nums:
        # calculate the max value at current position
        curr = max(num + left, right)
        # move pointers
        left = right
        right = curr
    return right


res = house_robber([1, 2, 3, 1])
print(res)
