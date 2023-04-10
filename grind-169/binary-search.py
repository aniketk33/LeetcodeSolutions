def search(nums, target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

nums = [-1,0,3,5,9,12]
target = 2
result = search(nums, target)
print(result)
