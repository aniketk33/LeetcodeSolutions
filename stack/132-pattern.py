def find_pattern(nums):
    # stores the num and the min value to its left
    stack = []
    curr_min = nums[0]

    for curr_num in nums[1:]:
        # pop if the elements are smaller than the current num
        while stack and stack[-1][0] <= curr_num:
            stack.pop()

        # check if the last element's min value is less than the current value
        if stack and stack[-1][1] < curr_num:
            return True

        stack.append([curr_num, curr_min])
        curr_min = min(curr_min, curr_num)

    return False


res = find_pattern([-1, 3, 2, 0])
print(res)
