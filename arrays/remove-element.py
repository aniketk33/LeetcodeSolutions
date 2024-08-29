def remove_element(nums, val):
    left_ptr = 0

    for i in range(len(nums)):
        # swap at position left_ptr if the given value is not equal to the value to be deleted
        if nums[i] != val:
            nums[left_ptr] = nums[i]
            left_ptr += 1

    return left_ptr


def remove_element_2(nums, val):
    left, right = 0, 0

    while right < len(nums):
        if nums[left] != val:
            left += 1
            right += 1
        else:
            # get the next value not eq val
            while right < len(nums) and nums[right] == val:
                right += 1
            if len(nums) == right:
                return left
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right = left

    return left


res = remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2)
# res = remove_element_2([2], 3)
print(res)
