def three_sum(num_arr):
    arr_len = len(num_arr)
    num_arr.sort()
    result = []

    for index, val in enumerate(num_arr):
        if index > 0 and val == num_arr[index - 1]:
            continue

        left_ptr, right_ptr = index + 1, arr_len - 1
        while left_ptr < right_ptr:
            nums_sum = val + num_arr[left_ptr] + num_arr[right_ptr]
            if nums_sum == 0:
                result.append([val, num_arr[left_ptr], num_arr[right_ptr]])
                left_ptr += 1
                # EDGE CASE: while shifting the left pointer, if we encounter the same next value,
                # we have to keep moving the left pointer until we find the next unique value
                while num_arr[left_ptr] == num_arr[left_ptr - 1] and left_ptr < right_ptr:
                    left_ptr += 1
            elif nums_sum > 0:
                right_ptr -= 1
            else:
                left_ptr += 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
res = three_sum(nums)
print(res)
