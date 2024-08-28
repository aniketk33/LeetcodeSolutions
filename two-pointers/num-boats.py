# solution using O(nlog(n)) and constant space
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


# solution using O(n) time and space
def num_boats_2(people, limit):
    # why limit + 1?
    # because all the values in the array would be less than or equal to limit
    # and array starts with index 0, so +1 to match the upper bound
    frequency = [0] * (limit + 1)

    for val in people:
        frequency[val] += 1

    # left and right are basically the values from the people array.
    # they are treated as index in the frequency array
    left, right = 0, limit
    boats = 0

    while left <= right:
        # ignoring all the zero frequencies
        while left <= right and frequency[left] <= 0:
            left += 1
        while left <= right and frequency[right] <= 0:
            right -= 1

        # if the smaller value surpasses the bigger value,
        # then break out of the loop as there are no valid pairs remaining
        if left > right:
            break

        if left + right <= limit:
            frequency[left] -= 1
            frequency[right] -= 1
        else:
            frequency[right] -= 1

        boats += 1

    return boats


# res = num_boats([3, 5, 3, 4], 5)
res = num_boats_2([2, 4], 5)
print(res)
