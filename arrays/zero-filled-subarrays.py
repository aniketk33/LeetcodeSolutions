def zero_filled(nums):
    consecutive_count, result = 0, 0

    for i in range(len(nums)):
        if nums[i] == 0:
            consecutive_count += 1
        else:
            # reset the count
            consecutive_count = 0

        # add the current consecutive count of zeroes
        result += consecutive_count

    return result


res = zero_filled([1, 3, 0, 0, 2, 0, 0, 4])
print(res)
