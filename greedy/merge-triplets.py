def merge_triplets(triplets, target):
    result = set()

    for curr_triplet in triplets:
        # check if any of the value of the current triplet is greater than the target's value
        if curr_triplet[0] > target[0] or curr_triplet[1] > target[1] or curr_triplet[2] > target[2]:
            continue

        for i, val in enumerate(curr_triplet):
            if val == target[i]:
                result.add(i)

    # if found, then return
    return len(result) == 3


res = merge_triplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5])
print(res)
