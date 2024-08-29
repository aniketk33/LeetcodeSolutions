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

    for i in range(arr_len - 1, -1, -1):
        # get the curr element
        curr_element = arr[i]
        # replace it with the max element
        arr[i] = max_element
        # update the max value
        max_element = max(max_element, curr_element)

    return arr


def replace_element_3(arr):
    # returns the new max index and val
    def get_max(start_idx):
        new_max_val = -1
        new_max_idx = -1
        for idx in range(start_idx, len(arr)):
            val = arr[idx]
            if val > new_max_val:
                new_max_val = val
                new_max_idx = idx

        return new_max_idx, new_max_val

    max_idx, max_val = get_max(0)

    for i in range(len(arr) - 1):
        if max_idx > i:
            arr[i] = max_val
        else:
            max_idx, max_val = get_max(i + 1)
            arr[i] = max_val

    arr[-1] = -1

    return arr


# res = replace_element_2([17, 18, 5, 4, 6, 1])
res = replace_element_3([17, 18, 5, 4, 6, 1])
print(res)
