class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        # return the index if the target is found
        if target in nums:
            return nums.index(target)

        # return the position where it could be added in the list if not found
        nums.append(target)
        nums.sort()
        return nums.index(target)
        
        # for i in range(len(nums)):
        #     if i == len(nums)-1:
        #         if target > nums[i]:
        #             return i+1
        #         return i
            
        #     if target < nums[i]:
        #         return i
        #     elif target > nums[i] and target < nums[i+1]:
        #         return i+1
            

nums = [1,3,5,6]
target = 0
output = Solution().searchInsert(nums, target)
print(output)