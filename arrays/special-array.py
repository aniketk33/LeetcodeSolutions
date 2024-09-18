from collections import defaultdict


# brute force approach
def special_array(nums):
    count = defaultdict(int)

    for i in range(len(nums) + 1):
        for num in nums:
            if num >= i:
                count[i] += 1
        if count[i] == i:
            return i

    return -1


def special_array_2(nums):
    arr_len = len(nums)
    count = [0] * (arr_len + 1)

    # create the index count for every num
    for num in nums:
        if num >= arr_len:
            count[arr_len] += 1
        else:
            count[num] += 1

    # check if the sum of right indices is equal to the current index
    right_sum = 0
    for i in range(len(count) - 1, -1, -1):
        right_sum += count[i]
        if right_sum == i:
            return i

    return -1


# res = special_array([0, 4, 3, 0, 4])
res = special_array_2([3, 5])
print(res)
