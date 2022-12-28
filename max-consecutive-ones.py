'''Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result = 0
        temp_res = 0
        for num in nums:
            if num == 1:
                temp_res += 1
                if temp_res > result:
                    result = temp_res
                continue
            if temp_res > result:
                result = temp_res
            temp_res = 0
        return result

nums = [1,1,0,1,1,1]
soln = Solution().findMaxConsecutiveOnes(nums)
print(soln)