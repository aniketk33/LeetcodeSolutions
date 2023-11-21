def closet_elements(nums, target, window_size):
    left_ptr, right_ptr = 0, len(nums) - window_size

    while left_ptr < right_ptr:
        # find the mid-index
        mid_idx = left_ptr + (right_ptr - left_ptr) // 2

        # IMP POINT
        # check if the difference between target and mid_idx element is greater than the difference between right+1
        # and target element then move the left pointer to mid_idx+1 else right_ptr to mid_idx
        if (target - nums[mid_idx]) > (nums[mid_idx + window_size] - target):
            left_ptr = mid_idx + 1
        else:
            right_ptr = mid_idx

    return nums[left_ptr:left_ptr + window_size]


res = closet_elements([1, 2, 3, 4, 5], 5, 2)
print(res)
