def product_array(num_arr):
    arr_len = len(num_arr)
    prefix = 1
    output = [prefix]
    # calculate prefix
    for i in range(1, arr_len):
        val = prefix * num_arr[i - 1]
        output.append(val)
        prefix = val
    # multiply last element to output array
    postfix = 1
    output[-1] *= postfix
    postfix *= num_arr[-1]
    # calculate postfix
    for i in range(arr_len - 1, 0, -1):
        val = output[i - 1] * postfix
        output[i - 1] = val
        postfix *= num_arr[i - 1]

    return output


arr = [4, 3, 2, 1, 2]
res = product_array(arr)
print(res)
