def two_sum_2(num_arr, target):
    arr_len = len(num_arr)
    left_ptr, right_ptr = 0, arr_len - 1
    while left_ptr <= right_ptr:
        value = num_arr[left_ptr] + num_arr[right_ptr]
        if value == target:
            return [left_ptr+1, right_ptr+1]
        if value > target:
            right_ptr -= 1
        else:
            left_ptr += 1


arr = [-1,0]
tar = -1
res = two_sum_2(arr, tar)
print(res)
