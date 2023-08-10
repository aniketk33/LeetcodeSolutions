"""Given an array of distinct integers candidates and a target integer target, return a list of all unique
combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150
combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""


def combination_sum(num_arr, target):
    num_arr.sort()  # sort the array to make the process easy to remove duplicates
    result = []

    def dfs(nums, start_idx, remaining_target, path):
        if remaining_target == 0:
            result.append(path[:])

        for i in range(start_idx, len(nums)):
            num = nums[i]
            if remaining_target - num < 0:
                continue
            dfs(nums, i, remaining_target - num, path + [num])

    dfs(num_arr, 0, target, [])
    return result


arr = [2, 3, 6, 7]
tar = 7
res = combination_sum(arr, tar)
print(res)
