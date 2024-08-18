from collections import Counter


def LHS(nums):
    num_counter = Counter(nums)
    longest = 0

    for key, val in num_counter.items():
        # check for the next number in the dict to form the longest sequence
        if key + 1 in num_counter:
            longest = max(longest, num_counter[key + 1] + val)

    return longest


res = LHS([1, 3, 2, 2, 5, 2, 3, 7])
print(res)
