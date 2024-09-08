import math


def koko(piles, h):
    # this is the max bananas she can have at once
    max_val = max(piles)
    # define the range
    left_ptr, right_ptr = 1, max_val
    result = max_val

    while left_ptr <= right_ptr:
        # select random banana b/w the range
        k = left_ptr + (right_ptr - left_ptr) // 2
        eating_time = 0
        for banana in piles:
            eating_time += math.ceil(banana / k)

        if eating_time <= h:
            # result = min(result, k)
            # this improves time complexity drastically
            if result > k:
                result = k
            right_ptr = k - 1
        else:
            left_ptr = k + 1

    return result


res = koko([3, 6, 7, 11], 8)
print(res)
