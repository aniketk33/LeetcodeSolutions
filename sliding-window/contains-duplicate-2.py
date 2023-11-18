def contains_duplicate(nums, k):
    window = set()
    left_ptr = 0

    for right_ptr in range(len(nums)):
        # check if the window size is greater than the given size
        if right_ptr - left_ptr > k:
            # if yes, then remove the left element and increment the pointer
            window.remove(nums[left_ptr])
            left_ptr += 1

        # return True if the right element already exists within the window length
        if nums[right_ptr] in window:
            return True
        # keep adding the elements
        window.add(nums[right_ptr])

    return False


res = contains_duplicate([1, 2, 3, 1], 1)
print(res)
