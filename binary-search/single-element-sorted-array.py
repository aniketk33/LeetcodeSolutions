def single_element(nums):
    left_ptr, right_ptr = 0, len(nums) - 1

    while left_ptr <= right_ptr:
        mid = left_ptr + (right_ptr - left_ptr) // 2

        if (mid - 1 < 0 or nums[mid] != nums[mid - 1]) and (mid + 1 >= len(nums) or nums[mid] != nums[mid + 1]):
            return nums[mid]

        if nums[mid - 1] == nums[mid]:
            left_size = mid - 1
        else:
            left_size = mid

        # check if it is even or odd and then move the pointer accordingly
        if left_size % 2 == 0:
            left_ptr = mid + 1
        else:
            right_ptr = mid - 1


res = single_element([1, 1, 2, 3, 3, 4, 4, 8, 8])
print(res)
