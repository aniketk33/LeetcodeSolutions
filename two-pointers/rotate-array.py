def rotate_array(nums, k):
    # how many times the array should be rotated
    k = k % len(nums)

    def reverse_array(left_ptr, right_ptr):
        while left_ptr < right_ptr:
            nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
            left_ptr += 1
            right_ptr -= 1

    # initially reverse the array
    reverse_array(0, len(nums) - 1)

    # reverse the array up to k-elements
    reverse_array(0, k - 1)

    # reverse the next half of the array
    reverse_array(k, len(nums) - 1)
