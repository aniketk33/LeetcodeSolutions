def check(nums):
    arr_len = len(nums)
    rotation = 0
    for i in range(arr_len):
        # keep traversing until the curr is greater than prev
        if nums[(i + 1) % arr_len] >= nums[i]:
            continue
        rotation += 1
        # only one prev number will be greater than the current number as it can be a rotated array
        if rotation > 1:
            return False

    return True


res = check([4, 5, 1, 2, 3])
print(res)
