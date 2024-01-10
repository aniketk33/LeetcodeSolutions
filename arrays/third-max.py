def third_max(nums):
    first, second, third = float('-inf'), float('-inf'), float('-inf')

    for num in nums:
        # keep moving the numbers to the right
        if num > first:
            first, second, third = num, first, second
        elif first > num > second:
            second, third = num, second
        elif second > num > third:
            third = num

    return third if third != float('-inf') else first


res = third_max([1, 2])
print(res)
