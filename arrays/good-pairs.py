def good_pairs(nums):
    result = 0
    count_pairs = {}

    # get the count of each num
    for val in nums:
        count_pairs[val] = 1 + count_pairs.get(val, 0)

    for key, val in count_pairs.items():
        if val == 1:
            continue
        # count pairs formula
        result += (val * (val - 1)) // 2

    return result


res = good_pairs([1, 2, 3, 1, 1, 3])
print(res)
