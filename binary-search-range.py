'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.'''


def binary_search_range(nums_arr, target):
    left, right = 0, len(nums_arr) - 1
    left_pos, right_pos = -1, -1

    # for left position
    while left <= right:
        mid = (left + right) // 2
        if nums_arr[mid] == target:
            left_pos = mid
            right = mid - 1
        elif nums_arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    # for right position (do not forget to re-initialize the left and right position!!)
    left, right = 0, len(nums_arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums_arr[mid] == target:
            right_pos = mid
            left = mid + 1
        elif nums_arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left_pos, right_pos


nums = [5, 7, 7, 8, 8, 10]
target = 8
result = binary_search_range(nums, target)
print(result)
