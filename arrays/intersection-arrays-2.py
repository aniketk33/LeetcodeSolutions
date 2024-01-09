# arrays are sorted
def intersection_array(nums1, nums2):
    nums1.sort()
    nums2.sort()
    left_ptr, right_ptr = 0, 0
    result = []

    while left_ptr < len(nums1) and right_ptr < len(nums2):
        if nums1[left_ptr] == nums2[right_ptr]:
            result.append(nums1[left_ptr])
            left_ptr += 1
            right_ptr += 1
        elif nums1[left_ptr] > nums2[right_ptr]:
            right_ptr += 1
        else:
            left_ptr += 1

    return result


res = intersection_array([1, 2, 2, 1], [2, 2])
print(res)
