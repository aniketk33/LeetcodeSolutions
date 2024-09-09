"""Search in Rotated Sorted Array Given the array nums after the possible rotation and an integer target, return the
index of target if it is in nums, or -1 if it is not in nums."""


def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def search(num_arr, target) -> int:
    n = len(num_arr)
    left, right = 0, n - 1
    min_index = -1
    # to find the minimum index in the array
    while left <= right:
        mid = (left + right) // 2
        if num_arr[mid] == target:
            return mid
        prev_num = ((mid + n) - 1) % n
        next_num = (mid + 1) % n
        if num_arr[prev_num] > num_arr[mid] and num_arr[next_num] > num_arr[mid]:
            min_index = mid
            break
        elif num_arr[mid] < num_arr[-1]:
            right = mid - 1
        else:
            left = mid + 1

    # search in the subarray
    if target >= num_arr[0] and target > num_arr[min_index]:
        target_index = binary_search(num_arr, left=0, right=((min_index + n) - 1) % n, target=target)
    else:
        target_index = binary_search(num_arr, left=min_index, right=n - 1, target=target)

    return target_index


def search_2(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        # determine which side is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


res = search_2([4, 5, 6, 7, 0, 1, 2], 0)
print(res)
