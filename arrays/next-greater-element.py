def next_greater(nums1, nums2):
    result = [-1] * len(nums1)

    # hashmap to store the value and index of nums1 array
    nums_dict = {num: idx for idx, num in enumerate(nums1)}

    for i in range(len(nums2)):
        # if the nums2 element is not present in the nums1 dict then just ignore
        if nums2[i] not in nums_dict:
            continue
        curr_idx = i + 1
        for j in range(curr_idx, len(nums2)):
            # if the current num is greater than the previous num, then place it in the result array
            if nums2[j] > nums2[i]:
                previous_num_idx = nums_dict[nums2[i]]
                result[previous_num_idx] = nums2[j]
                break

    return result


# efficient solution O(n)
def next_greater_2(nums1, nums2):
    result = [-1] * len(nums1)
    stack = []

    # hashmap to store the value and index of nums1 array
    nums_dict = {num: idx for idx, num in enumerate(nums1)}

    for i in range(len(nums2)):
        curr_val = nums2[i]
        # check if the stack is non-empty and the current value is greater,
        # then the last value in the stack
        while stack and curr_val > stack[-1]:
            val = stack.pop()
            idx = nums_dict[val]
            result[idx] = curr_val

        # add when the value exists in the nums1 array
        if curr_val in nums_dict:
            stack.append(curr_val)

    return result


res = next_greater_2([4, 1, 2], [2, 1, 3, 4])
print(res)
