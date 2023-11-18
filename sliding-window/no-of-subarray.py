def no_of_subarray(nums, window_size, threshold):
    count = 0
    # get the sum of the elements within the window_size - 1
    curr_sum = sum(nums[:window_size - 1])

    # start from the next window_size
    for left_ptr in range(len(nums) - window_size + 1):
        # add the next element in the current sum within the window_size
        next_element = nums[left_ptr + window_size - 1]
        curr_sum += next_element

        # calculate the average
        average = curr_sum / window_size
        if average >= threshold:
            count += 1

        # remove the left most element from the window
        curr_sum -= nums[left_ptr]

    return count


res = no_of_subarray([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
print(res)
