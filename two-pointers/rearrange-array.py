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


# optimal approach without sorting array and constant space
def rearrange_2(nums):
    for idx in range(1, len(nums) - 1):
        prev = nums[idx - 1]
        curr = nums[idx]
        next = nums[idx + 1]

        # swap the current with next only when this condition is satisfied
        if prev < curr < next or prev > curr > next:
            nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]

    return nums


# res = rearrange([6, 2, 0, 9, 7])
res = rearrange_2([6, 2, 0, 9, 7])
print(res)
