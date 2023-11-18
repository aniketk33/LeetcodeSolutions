def rearrange(nums):
    nums.sort()
    result = []

    left_ptr, right_ptr = 0, len(nums) - 1

    while len(result) != len(nums):
        # add the smallest element first
        result.append(nums[left_ptr])
        left_ptr += 1

        # only add the greater element when the left pointer is less than the right pointer
        if left_ptr <= right_ptr:
            result.append(nums[right_ptr])
            right_ptr -= 1

    return result


res = rearrange([6, 2, 0, 9, 7])
print(res)
