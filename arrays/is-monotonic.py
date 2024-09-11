def is_monotonic(nums):
    is_increasing = False
    n = len(nums)

    # find out whether the array is increasing or decreasing
    j = 0
    while j < n - 1:
        if nums[j] < nums[j + 1]:
            is_increasing = True
            break
        j += 1

    if j == n - 1 and not is_increasing:
        return True

    i = 0
    while i < n - 1 and nums[i] <= nums[i + 1]:
        i += 1

    return i == n - 1


res = is_monotonic([1, 2, 3])
print(res)
