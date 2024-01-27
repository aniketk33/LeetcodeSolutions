def longest(nums):
    # store the LIS and its count
    cache = {}
    lis, result = 0, 0

    for i in range(len(nums) - 1, -1, -1):
        curr_max_lis, curr_max_count = 1, 1
        # start from the next index
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                curr_lis, count = cache[j]
                if 1 + curr_lis > curr_max_lis:
                    curr_max_lis, curr_max_count = 1 + curr_lis, count
                elif 1 + curr_lis == curr_max_lis:
                    curr_max_count += count
        # keep track of the result
        if curr_max_lis > lis:
            lis, result = curr_max_lis, curr_max_count
        elif curr_max_lis == lis:
            result += curr_max_count
        cache[i] = [curr_max_lis, curr_max_count]

    return result


res = longest([1, 3, 5, 4, 7])
print(res)
