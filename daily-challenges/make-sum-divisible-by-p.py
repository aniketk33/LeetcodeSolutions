from collections import defaultdict


def divisible(nums, p):
    remainder = sum(nums) % p
    # if there is no need to remove any subarray
    if remainder == 0:
        return 0

    prefix_sum = 0
    min_len = len(nums)
    remainder_count = defaultdict(int)
    # we are storing the remainder and their position
    remainder_count[0] = -1

    for i, val in enumerate(nums):
        prefix_sum += val
        curr_remainder = prefix_sum % p
        target_remainder = (curr_remainder - remainder + p) % p
        # only store the length when the target remainder is present
        if target_remainder in remainder_count and min_len > i - remainder_count[target_remainder]:
            min_len = i - remainder_count[target_remainder]
        remainder_count[curr_remainder] = i

    return -1 if min_len == len(nums) else min_len


res = divisible([3, 1, 4, 2], 6)
print(res)
