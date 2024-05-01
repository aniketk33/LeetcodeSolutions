def longest_subarray(nums, k):
    longest = 0
    # store sum and index location
    sum_dict = {}
    curr_sum = 0

    for idx, num in enumerate(nums):
        curr_sum += num
        if curr_sum == k:
            longest = max(longest, idx + 1)
        # check for prev stored values in the stack
        diff = curr_sum - k
        if diff in sum_dict:
            longest = max(longest, idx - sum_dict[diff])

        # we do not have to update the idx when we encounter a zero
        if curr_sum not in sum_dict:
            sum_dict[curr_sum] = idx

    return longest


# two pointer approach
def longest_subarray_2(nums, k):
    left, right, curr_sum = 0, 0, 0
    longest = 0
    while right < len(nums):
        curr_sum += nums[right]
        if curr_sum == k:
            longest = max(longest, right - left + 1)
        elif curr_sum > k:
            while left < len(nums) and curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == k:
                longest = max(longest, right - left + 1)
        right += 1

    return longest


res = longest_subarray_2([1, 2, 3, 1, 1, 1, 1], 3)
# edge case scenario
# res = longest_subarray_2([2, 0, 0, 3], 3)
print(res)
