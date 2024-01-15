def search(nums, target):
    left_ptr, right_ptr = 0, len(nums) - 1

    while left_ptr <= right_ptr:
        mid = left_ptr + (right_ptr - left_ptr) // 2

        if nums[mid] == target:
            return True

        # left portion
        if nums[left_ptr] < nums[mid]:
            if nums[left_ptr] <= target < nums[mid]:
                right_ptr = mid - 1
            else:
                left_ptr = mid + 1
        # right portion
        elif nums[left_ptr] > nums[mid]:
            if nums[mid] < target <= nums[right_ptr]:
                left_ptr = mid + 1
            else:
                right_ptr = mid - 1
        else:
            # skip the duplicates
            left_ptr += 1

    return False


res = search([2, 5, 6, 0, 0, 1, 2], 0)
print(res)
