import heapq


def last_stone_weight(num_arr):
    # base case
    if len(num_arr) == 1:
        return num_arr[0]
    # create a heap with negative values
    num_arr = [-num for num in num_arr]
    heapq.heapify(num_arr)

    while len(num_arr) > 1:
        first_val, second_val = heapq.heappop(num_arr), heapq.heappop(num_arr)
        first_val *= -1
        second_val *= -1
        diff = first_val - second_val
        heapq.heappush(num_arr, -diff)

    return -num_arr[0]


arr = [3, 7, 2]
res = last_stone_weight(arr)
print(res)
