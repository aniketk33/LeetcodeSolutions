from collections import Counter


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


# optimal solution
def good_pairs_2(nums):
    count = Counter(nums)
    pairs = 0

    for key, val in count.items():
        if val <= 1:
            continue
        pairs += (val * (val - 1)) // 2

    return pairs
    # OR
    # count = defaultdict(int)
    # pairs = 0
    #
    # for num in nums:
    #     count[num] += 1
    #     pairs += count[num] - 1
    #
    # return pairs


# res = good_pairs([1, 2, 3, 1, 1, 3])
res = good_pairs_2([1, 2, 3, 1, 1, 3])
print(res)
