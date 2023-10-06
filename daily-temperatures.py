def daily_temperatures(temp_arr):
    arr_len = len(temp_arr)
    result = [0] * arr_len

    # to store the current temps and index
    stack = []
    for index, temp in enumerate(temp_arr):
        # to check whether the stack is empty and last added temp is greater than current
        while stack and temp > stack[-1][0]:
            _, idx = stack.pop()
            diff = index - idx
            result[idx] = diff

        stack.append([temp, index])

    return result


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
res = daily_temperatures(temperatures)
print(res)
