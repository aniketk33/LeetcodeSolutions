def subarray_sum(arr, target):
    # prefix sum starts with 0th index
    prefix_sum = {0: 0}
    curr_sum = 0

    for idx, num in enumerate(arr):
        curr_sum += num
        compliment = curr_sum - target
        if compliment in prefix_sum:
            return [prefix_sum[compliment], idx + 1]
        # why +1? as we have to add from the 1st index position
        prefix_sum[curr_sum] = idx + 1


res = subarray_sum([1, 3, -3, 8, 5, 7], 5)
# res = subarray_sum([1, -20, -3, 30, 5, 4], 7)
print(res)
