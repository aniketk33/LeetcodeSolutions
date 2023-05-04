"""A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time."""


def find_peak_element(num_arr):
    n = len(num_arr)
    # for single element in the array
    if n == 1:
        return 0

    # for 2 and 3 elements in the array
    if num_arr[0] > num_arr[1]:
        return 0

    if num_arr[n - 1] > num_arr[n - 2]:
        return n - 1

    left, right = 0, n - 1
    while left <= right:
        mid_index = left + (right - left) // 2
        prev_num_index = (mid_index - 1 + n) % n
        next_num_index = (mid_index + 1) % n
        if num_arr[prev_num_index] < num_arr[mid_index] > num_arr[next_num_index]:
            return mid_index
        if num_arr[mid_index] > num_arr[next_num_index]:
            right = mid_index - 1
        else:
            left = mid_index + 1
