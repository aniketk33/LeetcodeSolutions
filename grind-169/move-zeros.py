def move_zeros(arr):
    i = 0
    for num in arr:
        if num != 0:
            arr[i] = num
            i += 1

    while i < len(arr):
        arr[i] = 0
        i += 1


def move_zeros_2(arr):
    slow = fast = 0
    while fast < len(arr):
        # keep moving fast until non-zero value
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
        fast += 1


num_arr = [1, 0, 1]
# move_zeros(num_arr)
move_zeros_2(num_arr)
print(num_arr)
