def non_decreasing(nums):
    changed = False

    for i in range(len(nums) - 1):
        # already in increasing order
        if nums[i] <= nums[i + 1]:
            continue

        if changed:
            return False

        # change the arr[left] with arr[right] if the right element is greater than left-1
        # e.g., [1,3,2] will become [1,2,2]
        if i == 0 or nums[i + 1] >= nums[i - 1]:
            nums[i] = nums[i + 1]
        else:
            nums[i + 1] = nums[i]

        changed = True

    return True


res = non_decreasing([4, 2, 3])
print(res)
