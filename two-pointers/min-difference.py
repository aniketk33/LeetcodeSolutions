def min_difference(nums, k):
    # sort the array
    nums.sort()

    # initialize the window
    left_ptr, right_ptr = 0, k - 1
    result = float('inf')

    # right pointer shouldn't go out of bound
    while right_ptr < len(nums):
        diff = nums[right_ptr] - nums[left_ptr]
        result = min(result, diff)
        left_ptr += 1
        right_ptr += 1

    return result


res = min_difference([90], 1)
print(res)
