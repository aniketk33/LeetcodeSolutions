def sort_colors(nums):
    left_ptr, right_ptr = 0, len(nums) - 1
    curr_ptr = 0

    while curr_ptr <= right_ptr:
        if nums[curr_ptr] == 2:
            nums[right_ptr], nums[curr_ptr] = nums[curr_ptr], nums[right_ptr]
            right_ptr -= 1
            # we don't need to increment the curr_ptr while swapping with the rightmost element
            curr_ptr -= 1
        elif nums[curr_ptr] == 0:
            nums[left_ptr], nums[curr_ptr] = nums[curr_ptr], nums[left_ptr]
            left_ptr += 1
        curr_ptr += 1


num_arr = [2, 0, 2, 1, 1, 0]
print(f'Before sorting: {num_arr}')
sort_colors(num_arr)
print(f'After sorting: {num_arr}')
