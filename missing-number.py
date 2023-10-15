"""Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""


def missing_number(num_arr: list) -> int:
    # counting the length
    arr_len = len(num_arr)
    # get the total sum of N elements using (N*(N+1))//2 formula
    sum_of_all = arr_len * (arr_len + 1) // 2
    # by subtracting the sum of given arr and total sum, we get the missing number
    return sum_of_all - sum(num_arr)


nums = [3, 1, 0]
sol = missing_number(nums)
print(sol)
