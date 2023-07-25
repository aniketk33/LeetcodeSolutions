def move_zeros(num_arr):
    i = 0
    for num in num_arr:
        if num != 0:
            num_arr[i] = num
            i += 1

    while i < len(num_arr):
        num_arr[i] = 0
        i += 1


num_arr = [0,1,0,3,12]
move_zeros(num_arr)
print(num_arr)