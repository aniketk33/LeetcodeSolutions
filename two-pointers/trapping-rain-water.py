def trap_water(height_array):
    if not height_array:
        return 0
    left_ptr, right_ptr = 0, len(height_array) - 1
    max_left, max_right = height_array[left_ptr], height_array[right_ptr]
    water_capacity = 0

    while left_ptr <= right_ptr:
        # move the pointer which has min value
        if max_left <= max_right:
            curr_height = height_array[left_ptr]
            # formula
            diff = max_left - curr_height
            if diff >= 0:
                water_capacity += diff
            max_left = max(max_left, curr_height)
            left_ptr += 1
        else:
            curr_height = height_array[right_ptr]
            diff = max_right - curr_height
            if diff >= 0:
                water_capacity += diff
            max_right = max(max_right, curr_height)
            right_ptr -= 1

    return water_capacity


res = trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(res)
