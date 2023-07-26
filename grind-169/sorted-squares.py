"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted
in non-decreasing order.

Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different
approach?

"""


def sorted_squares(num_arr):
    sorted()
    arr_len = len(num_arr)
    if arr_len == 1:
        return [num_arr[0] ** 2]
    left_ptr, right_ptr = 0, arr_len - 1
    result = []
    while right_ptr >= left_ptr:
        if num_arr[left_ptr] ** 2 > num_arr[right_ptr] ** 2:
            result.insert(0, num_arr[left_ptr] ** 2)
            left_ptr += 1
        else:
            result.insert(0, num_arr[right_ptr] ** 2)
            right_ptr -= 1

    return result


nums = [-7, -3, 2, 3, 11]
res = sorted_squares(nums)
print(res)
