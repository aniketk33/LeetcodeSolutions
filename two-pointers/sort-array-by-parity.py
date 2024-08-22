def sort_array(nums):
    left, right = 0, len(nums) - 1

    while left <= right:
        # if left is even, move the left pointer
        if nums[left] % 2 == 0:
            left += 1
        # if right is odd, move only the right pointer
        elif nums[right] % 2 == 1:
            right -= 1
        # if left is odd and right is even, then swap places
        elif nums[left] % 2 == 1 and nums[right] % 2 == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        else:
            left += 1
            right -= 1

    return nums


res = sort_array([3, 1, 2, 4])
print(res)
