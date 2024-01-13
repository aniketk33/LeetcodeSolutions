def arrange_coins(n):
    left_ptr, right_ptr = 1, n
    result = 0

    while left_ptr <= right_ptr:
        mid = left_ptr + (right_ptr - left_ptr) // 2
        coins = (mid * (mid + 1)) / 2
        if coins > n:
            right_ptr = mid - 1
        else:
            left_ptr = mid + 1
            result = max(result, mid)

    return result


res = arrange_coins(5)
print(res)
