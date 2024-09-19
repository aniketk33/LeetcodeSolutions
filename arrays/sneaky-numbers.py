# brute force approach with O(n) time and space
from collections import defaultdict


def sneaky_numbers(nums):
    check_arr = [1] * len(nums)
    result = []

    for num in nums:
        if check_arr[num] < 0:
            result.append(num)
        check_arr[num] = -check_arr[num]

    return result


# optimal solution
def sneaky_numbers_2(nums):
    check = defaultdict(int)
    result = []

    for num in nums:
        check[num] += 1
        if check[num] >= 2:
            result.append(num)

    return result


# res = sneaky_numbers([0, 3, 2, 1, 3, 2])
res = sneaky_numbers_2([0, 3, 2, 1, 3, 2])
print(res)
