def remove_element(nums, val):
    left_ptr = 0

    for i in range(len(nums)):
        # swap at position left_ptr if the given value is not equal to the value to be deleted
        if nums[i] != val:
            nums[left_ptr] = nums[i]
            left_ptr += 1

    return left_ptr


res = remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(res)
