from collections import defaultdict


def degree_subarray(nums):
    # keep track of the first and last occurrence along with the count of each num
    left, right, count = {}, {}, defaultdict(int)

    for idx, num in enumerate(nums):
        # do not update the left if occurrence is more than one
        if num not in left:
            left[num] = idx
        right[num] = idx
        count[num] += 1

    result = len(nums)
    # max frequency
    degree = max(count.values())
    # iterate over each count and return the min value amongst them
    for key, value in count.items():
        if value == degree:
            diff = right[key] - left[key] + 1
            if result > diff:
                result = diff

    return result


res = degree_subarray([1, 2, 2, 3, 1, 4, 2])
print(res)
