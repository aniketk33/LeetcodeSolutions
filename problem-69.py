"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

"""


def find_sqrt(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    sqrt = 0
    num_arr = [i for i in range(1, (num // 2 + 1))]
    n = len(num_arr)
    left, right = 0, n - 1
    while left <= right:
        mid_index = left + (right - left) // 2
        if num_arr[mid_index] * num_arr[mid_index] <= num:
            sqrt = num_arr[mid_index]
            left = mid_index + 1
        else:
            right = mid_index - 1

    return sqrt


num = 2147395599
res = find_sqrt(num)
print(f"Approx square root of {num} is {res}")
