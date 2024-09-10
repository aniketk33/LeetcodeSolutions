def min_sorted(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        # compare only with the right most element
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


# much optimal solution
def min_sorted_2(nums):
    n = len(nums)
    left, right = 0, n - 1

    while left < right:
        mid = left + (right - left) // 2
        prev_idx = (mid - 1 + n) % n
        next_idx = (mid + 1) % n
        # check if prev and next are larger values than current
        if nums[prev_idx] > nums[mid] < nums[next_idx]:
            return nums[mid]
        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            right = mid

    # if there is only a single element left in the array
    return nums[left]


res = min_sorted([1, 2, 3, 4, 5])
print(res)
