def num_boats(nums, limit):
    nums.sort()
    left_ptr, right_ptr = 0, len(nums) - 1
    boat_count = 0

    while left_ptr <= right_ptr:
        # if the sum is less than or equal to limit then only increment the boat count
        if nums[left_ptr] + nums[right_ptr] <= limit:
            left_ptr += 1
        boat_count += 1
        right_ptr -= 1

    return boat_count


res = num_boats([3, 5, 3, 4], 5)
print(res)
