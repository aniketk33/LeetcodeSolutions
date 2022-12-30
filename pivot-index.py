'''Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

'''
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        index = -1        
        for i in range(len(nums)):
            sum_prev_elements = 0 if i==0 else sum(nums[0:i])
            sum_next_elements = sum(nums[i+1:])
            if sum_prev_elements == sum_next_elements:
                index = i
                break
        
        return index

nums = [0]
soln = Solution().pivotIndex(nums)
print(soln)