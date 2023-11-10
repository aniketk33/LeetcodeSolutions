# the time limit exceeds for this solution if we iterate from the beginning
# as we have to recalculate the max each time we iterate from the same index
def replace_element(arr):
    arr_len = len(arr)
    result = []

    for i in range(arr_len - 1):
        max_among_remaining = max(arr[i + 1:])
        result.append(max_among_remaining)

    result.append(-1)

    return result


def replace_element_2(arr):
    arr_len = len(arr)
    max_element = -1

    for i in range(arr_len-1, -1, -1):
        # get the curr element
        curr_element = arr[i]
        # replace with the max element
        arr[i] = max_element
        # update the max value
        max_element = max(max_element, curr_element)

    return arr


res = replace_element_2([17, 18, 5, 4, 6, 1])
print(res)
