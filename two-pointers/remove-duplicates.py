def remove_duplicates(num_arr):
    left_ptr, right_ptr = 0, 0
    while right_ptr < len(num_arr):
        # move only the right pointer if you encounter a duplicate value
        if num_arr[left_ptr] == num_arr[right_ptr]:
            right_ptr += 1
            continue
        # if the unique element found then move the left pointer first and
        # then replace its value with the unique value
        left_ptr += 1
        num_arr[left_ptr] = num_arr[right_ptr]

    return left_ptr + 1


arr = [0, 0, 1, 1, 1, 2, 2, 3]
print(f'Array before duplicates removal: {arr}')
res = remove_duplicates(arr)
print(f'Array after duplicates removal: {arr[:res]}')
