def search(nums, target):
    left_ptr, right_ptr = 0, len(nums) - 1

    while left_ptr <= right_ptr:
        mid_idx = left_ptr + (right_ptr - left_ptr) // 2
        if nums[mid_idx] == target:
            return mid_idx
        if nums[mid_idx] > target:
            right_ptr = mid_idx - 1
        else:
            left_ptr = mid_idx + 1

    return right_ptr + 1


res = search([1, 3, 5, 6], 2)
print(res)
