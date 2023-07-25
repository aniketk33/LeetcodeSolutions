"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
always exists in the array.

Follow-up: Could you solve the problem in linear time and in O(1) space?

"""


def majority_element(num_arr):
    """Solution using Dictionary"""
    count = {}
    res_num = 0
    max_count = 0
    for n in num_arr:
        count[n] = 1 + count.get(n, 0)
        if count[n] > max_count:
            res_num = n
        max_count = max(max_count, count[n])

    return res_num


def majority_element_2(num_arr):
    res_num, count = 0, 0
    for n in num_arr:
        if count == 0:
            res_num = n
        count += (1 if n == res_num else -1)

    return res_num


nums = [6, 5, 5]
res = majority_element_2(nums)
print(res)
