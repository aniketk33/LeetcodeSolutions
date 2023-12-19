import math


def koko(piles, h):
    max_val = max(piles)
    left_ptr, right_ptr = 1, max_val
    result = max_val

    while left_ptr <= right_ptr:
        k = left_ptr + (right_ptr - left_ptr) // 2
        eating_time = 0
        for banana in piles:
            eating_time += math.ceil(banana / k)

        if eating_time <= h:
            result = min(result, k)
            right_ptr = k - 1
        else:
            left_ptr = k + 1

    return result


res = koko([312884470], 312884469)
print(res)
