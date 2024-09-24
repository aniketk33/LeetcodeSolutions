def dominant_index(nums):
    max_num = max(nums)
    result = 0

    for i, n in enumerate(nums):
        if n == max_num:
            result = i
            continue
        if n * 2 > max_num:
            return -1

    return result


def dominant_index_2(nums):
    sorted_arr = sorted(nums, reverse=True)
    if sorted_arr[0] >= sorted_arr[1] * 2:
        return nums.index(sorted_arr[0])
    return -1


def dominant_index_3(nums):
    max_idx = 0

    for i, n in enumerate(nums):
        if nums[i] > nums[max_idx]:
            max_idx = i

    for i, n in enumerate(nums):
        if i != max_idx and n * 2 > nums[max_idx]:
            return -1

    return max_idx


# res = dominant_index([1, 2, 3, 6])
# res = dominant_index_2([1, 2, 3, 6])
res = dominant_index_3([1, 2, 3, 6])
print(res)
