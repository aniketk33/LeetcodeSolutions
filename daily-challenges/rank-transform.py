from collections import defaultdict


# brute force approach
def rank_transform(arr):
    if len(arr) == 0:
        return arr
    rank = 1
    sorted_arr = sorted(arr)
    prev_num = sorted_arr[0]
    rank_dict = defaultdict(int)
    for i, curr_num in enumerate(sorted_arr):
        # only increment the rank when a larger num found and store the current largest
        if curr_num > prev_num:
            rank += 1
            prev_num = curr_num
        rank_dict[curr_num] = rank

    # assign the ranks to the original array
    for i, num in enumerate(arr):
        arr[i] = rank_dict[num]

    return arr


def rank_transform_2(arr):
    rank_dict = {}
    # get the unique values in sorted order
    sorted_arr = sorted(set(arr))

    for i, num in enumerate(sorted_arr):
        # ranks will be index + 1
        rank_dict[num] = i + 1

    return [rank_dict[n] for n in arr]


# res = rank_transform([40, 10, 20, 30])
res = rank_transform_2([40, 10, 20, 30])
print(res)
