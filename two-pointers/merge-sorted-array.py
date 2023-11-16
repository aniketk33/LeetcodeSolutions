from typing import List


def merge_array(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # last index of first array
    right_ptr = len(nums1) - 1

    while m > 0 and n > 0:
        if nums2[n - 1] > nums1[m - 1]:
            # replace it with array_2's value
            nums1[right_ptr] = nums2[n - 1]
            n -= 1
        else:
            # shift the array_1's value to the right
            nums1[right_ptr] = nums1[m - 1]
            m -= 1
        right_ptr -= 1

    # add the remaining elements of the second array
    while n > 0:
        nums1[right_ptr] = nums2[n - 1]
        right_ptr -= 1
        n -= 1


arr1 = [0]
arr2 = [1]
print(f'Array 1 before merging: {arr1}')
merge_array(arr1, 0, arr2, 1)
print(f'Array 1 after merging: {arr1}')
