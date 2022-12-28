'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: list) -> int:
        # counting the length
        N = len(nums)
        # get the total sum of N elements
        sum_of_all = N*(N+1)//2
        # by subtracting the sum of given arr and total sum, we get the missing number
        return sum_of_all - sum(nums)

nums = [3,1,0]
sol = Solution().missingNumber(nums)
print(sol)