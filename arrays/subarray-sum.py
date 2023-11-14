def subarray_sum(nums, k):
    result = 0
    sum_count_dict = {0: 1}
    curr_sum = 0

    for num in nums:
        curr_sum += num
        # get the difference from the current sum and given k
        difference = curr_sum - k

        # get the count from the dict and add to the result
        result += sum_count_dict.get(difference, 0)
        # update the count of the current sum
        sum_count_dict[curr_sum] = 1 + sum_count_dict.get(curr_sum, 0)

    return result


res = subarray_sum([1, 1, 1], 2)
print(res)
