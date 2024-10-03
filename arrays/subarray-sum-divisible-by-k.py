# brute force approach. TLE
from collections import defaultdict


def subarray(nums, k):
    count = 0
    for i in range(len(nums)):
        curr_sum = 0
        # check for every subarray including itself
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if curr_sum % k == 0:
                count += 1

    return count


def subarray_2(nums, k):
    remainder_count = defaultdict(int)
    remainder_count[0] = 1
    count = 0
    prefix_sum = 0

    for n in nums:
        prefix_sum += n
        remainder = prefix_sum % k
        # add the count of previously seen remainders to the count
        count += remainder_count[remainder]
        # increment the count for the current remainder
        remainder_count[remainder] += 1

    return count


def subarray_3(nums, k):
    # remainders will always be k-1
    remainders = [1] + [0] * (k - 1)
    count = prefix_sum = 0

    for n in nums:
        prefix_sum += n
        remainder = prefix_sum % k
        # add the count of previously seen remainders to the count
        count += remainders[remainder]
        # increment the count for the current remainder
        remainders[remainder] += 1

    return count


# res = subarray([4, 5, 0, -2, -3, 1], 5)
res = subarray_2([4, 5, 0, -2, -3, 1], 5)
print(res)
