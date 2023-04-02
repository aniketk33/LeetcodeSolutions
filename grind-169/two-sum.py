'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        map_nums = {}
        for i in range(len(nums)):
            # complement is the difference between target and the current number
            complement = target - nums[i]
            # checking if complement is in map_nums and if it is not the same index
            if complement in map_nums and map_nums[complement] != i:
                return [i, map_nums[complement]]
            map_nums[nums[i]] = i

nums = [3,2,4]
target = 6
soln = Solution().two_sum(nums, target)
print(soln)