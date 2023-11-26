def max_product(nums):
    curr_max, curr_min = 1, 1
    # if only a single element is present in the list
    result = max(nums)

    for num in nums:
        if num == 0:
            curr_max = curr_min = 1
            continue

        # get the previous curr_max stored in a temp variable
        temp = curr_max
        curr_max = max(num * curr_max, num * curr_min, num)
        curr_min = min(temp * num, num * curr_min, num)
        result = max(result, curr_max)

    return result


res = max_product([1, 2, 3, 0, 3, 5])
print(res)
