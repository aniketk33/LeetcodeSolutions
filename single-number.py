def single_number(num_arr):
    res = 0
    for num in num_arr:
        # XOR operation
        res = num ^ res

    return res


arr = [2, 2, 1]
result = single_number(arr)
print(result)
