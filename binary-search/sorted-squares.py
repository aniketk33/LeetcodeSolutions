def sorted_squares(num_arr):
    arr_len = len(num_arr)
    if arr_len == 1:
        return [num_arr[0] ** 2]
    left_ptr, right_ptr = 0, arr_len - 1
    result = []
    while right_ptr >= left_ptr:
        # append builds the list in descending order and insert builds in ascending order
        if num_arr[left_ptr] ** 2 > num_arr[right_ptr] ** 2:
            # result.insert(0, num_arr[left_ptr] ** 2)
            result.append(num_arr[left_ptr] ** 2)
            left_ptr += 1
        else:
            # result.insert(0, num_arr[right_ptr] ** 2)
            result.append(num_arr[right_ptr] ** 2)
            right_ptr -= 1

    # return result
    return result[::-1]


nums = [-7, -3, 2, 3, 11]
res = sorted_squares(nums)
print(res)
