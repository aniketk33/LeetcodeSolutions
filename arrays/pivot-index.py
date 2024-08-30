from typing import List


# inefficient solution
def pivot_index(nums: List[int]) -> int:
    index = -1
    for i in range(len(nums)):
        sum_prev_elements = 0 if i == 0 else sum(nums[0:i])
        sum_next_elements = sum(nums[i + 1:])
        if sum_prev_elements == sum_next_elements:
            index = i
            break

    return index


# much faster solution
def pivot_index_2(nums):
    left_sum = 0
    total_sum = sum(nums)  # O(n)

    for idx, num in enumerate(nums):
        right_sum = total_sum - left_sum - num
        if left_sum == right_sum:
            return idx
        left_sum += num

    return -1


def pivot_index_3(nums):
    prefix_arr = [0] * len(nums)
    postfix_arr = [0] * len(nums)
    prefix_sum = postfix_sum = 0

    # creating a prefix array
    for i in range(len(nums)):
        prefix_arr[i] += prefix_sum
        prefix_sum += nums[i]

    # creating a postfix array
    for i in range(len(nums) - 1, -1, -1):
        postfix_arr[i] += postfix_sum
        postfix_sum += nums[i]

    for i in range(len(nums)):
        if prefix_arr[i] == postfix_arr[i]:
            return i

    return -1


def pivot_index_4(nums):
    left, right = 0, sum(nums)

    for i, v in enumerate(nums):
        right -= v
        if left == right:
            return i
        left += v

    return -1


input_nums = [1, 7, 3, 6, 5, 6]
# res = pivot_index_2(input_nums)
# res = pivot_index_3(input_nums)
res = pivot_index_4(input_nums)
print(res)
