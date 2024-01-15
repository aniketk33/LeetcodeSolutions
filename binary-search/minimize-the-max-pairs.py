def minimize(nums, p):
    if p == 0:
        return 0

    def is_valid(threshold):
        curr_pairs, i = 0, 0
        while i < len(nums) - 1:
            if abs(nums[i] - nums[i + 1]) <= threshold:
                curr_pairs += 1
                i += 2
            else:
                i += 1
            if curr_pairs == p:
                return True

        return False

    nums.sort()
    left_ptr, right_ptr = 0, 10 ** 9
    result = 10 ** 9

    while left_ptr <= right_ptr:
        mid = left_ptr + (right_ptr - left_ptr) // 2
        if is_valid(mid):
            result = mid
            right_ptr = mid - 1
        else:
            left_ptr = mid + 1

    return result


res = minimize([10, 1, 2, 7, 1, 3], 2)
print(res)
