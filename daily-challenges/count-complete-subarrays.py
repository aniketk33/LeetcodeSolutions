# gives time limit exceeded error
from collections import defaultdict


def complete_subarrays(nums):
    # get the count of distinct's in the array
    distinct = len(set(nums))
    # total complete subarrays count
    complete = 0
    n = len(nums)

    for i in range(n):
        # the window will always be greater than total_distinct count
        curr_window = i + distinct
        while curr_window <= n:
            # get the distinct in the current window
            curr_distinct = set(nums[i:curr_window])
            if len(curr_distinct) == distinct:
                complete += 1
            curr_window += 1

    return complete


def complete_subarrays_2(nums):
    # get the count of distinct's in the array
    distinct = len(set(nums))
    # total complete subarrays count
    complete = 0
    n = len(nums)
    curr_window = defaultdict(int)
    right = 0

    for i in range(n):
        # decrement the count of left passed by elements from the current window
        if i > 0:
            curr_window[nums[i - 1]] -= 1
            if curr_window[nums[i - 1]] == 0:
                curr_window.pop(nums[i - 1])
        # keep adding elements until they are the same as total distinct
        while right < n and len(curr_window) < distinct:
            curr_window[nums[right]] += 1
            right += 1

        if len(curr_window) == distinct:
            complete += n - right + 1

    return complete


# res = complete_subarrays([1, 3, 1, 2, 2])
res = complete_subarrays_2([1, 3, 1, 2, 2])
print(res)
