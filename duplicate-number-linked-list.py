"""For better understanding refer FREEFORM"""


def duplicate_number(num_arr):
    slow_ptr, fast_ptr = 0, 0
    while True:
        # nums in the array points to location of next node
        # eg: [1,3,4,2,2]. at index 0 it is pointing to index 1 and at index 1 the next_node value
        # is index 3
        slow_ptr = num_arr[slow_ptr]
        fast_ptr = num_arr[num_arr[fast_ptr]]
        # breaking at the first checkpoint
        if slow_ptr == fast_ptr:
            break

    # the speed of both the pointers will move by 1
    slow_ptr_2 = 0
    while True:
        slow_ptr = num_arr[slow_ptr]
        slow_ptr_2 = num_arr[slow_ptr_2]
        # at the new intersection, the duplicate is found
        if slow_ptr == slow_ptr_2:
            return slow_ptr


arr = [1, 3, 4, 2, 2]
res = duplicate_number(arr)
print(res)
