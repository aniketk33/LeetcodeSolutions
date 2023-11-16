def remove_duplicates(nums):
    left_ptr, right_ptr = 0, 0

    while right_ptr < len(nums):
        curr_count = 1
        while right_ptr + 1 < len(nums) and nums[right_ptr] == nums[right_ptr + 1]:
            curr_count += 1
            right_ptr += 1

        # if a unique value is found, then replace until 2 places
        curr_count = min(curr_count, 2)
        for i in range(curr_count):
            nums[left_ptr] = nums[right_ptr]
            left_ptr += 1

        # move the right pointer to the next value
        right_ptr += 1

    return left_ptr


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3]
print(f'Array before duplicates removal: {arr}')
res = remove_duplicates(arr)
print(f'Array after duplicates removal: {arr[:res]}')
