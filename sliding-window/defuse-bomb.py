def defuse(code, k):
    arr_len = len(code)
    result = [0] * arr_len
    if k == 0:
        return result
    if k > 0:
        for idx, val in enumerate(code):
            window_sum = 0
            for i in range(1, k + 1):
                window_sum += code[(idx + i + arr_len) % arr_len]
            result[idx] = window_sum

        return result

    if k < 0:
        k *= -1
        for idx, val in enumerate(code):
            window_sum = 0
            for i in range(1, k + 1):
                window_sum += code[(idx - i + arr_len) % arr_len]
            result[idx] = window_sum

        return result


res = defuse([2, 4, 9, 3], -2)
print(res)
