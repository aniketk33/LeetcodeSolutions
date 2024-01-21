from collections import Counter


def delete_and_earn(nums):
    # keep count of the nums
    count = Counter(nums)
    # get the sorted unique values from the input nums
    nums = sorted(list(set(nums)))
    e1, e2 = 0, 0

    for i in range(len(nums)):
        curr_e = nums[i] * count[nums[i]]
        # check if previous is less than the current value by 1
        if i > 0 and nums[i] == nums[i - 1] + 1:
            temp = e2
            # get the previous earnings and add it to current and get the max from them and e2
            e2 = max(curr_e + e1, e2)
            e1 = temp
        else:
            temp = e2
            # add the current earnings
            e2 += curr_e
            e1 = temp

    return e2


res = delete_and_earn([2, 2, 3, 3, 3, 4])
print(res)
