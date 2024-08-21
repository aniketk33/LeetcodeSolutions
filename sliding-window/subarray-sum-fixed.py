def subarray_sum(nums, k):
    left, right = 0, k
    # first window
    curr_sum = sum(nums[:k])
    longest = curr_sum

    while right < len(nums):
        curr_sum -= nums[left]
        curr_sum += nums[right]
        # we have to include the last element
        longest = max(longest, curr_sum)
        left += 1
        right += 1

    return longest


res = subarray_sum([1, 2, 3, 7, 4, 1], 3)
print(res)
