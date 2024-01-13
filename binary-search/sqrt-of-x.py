def sqrt(x):
    left_ptr, right_ptr = 1, x
    result = 0

    while left_ptr <= right_ptr:
        mid = left_ptr + (right_ptr - left_ptr) // 2
        sq = mid ** 2
        if sq == x:
            return mid
        if sq > x:
            right_ptr = mid - 1
        else:
            result = mid
            left_ptr = mid + 1

    return result


res = sqrt(8)
print(res)
