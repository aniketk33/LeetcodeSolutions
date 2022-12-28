class Solution:
    def buildArray(self, nums):
        # return empty if input is null
        if nums is None:
            return None
        
        # assign the required values in the new list
        result = []
        for index in range(len(nums)):
            result.append(nums[nums[index]])
        
        # return the new list
        return result

input = [5,0,1,2,3,4]
soln = Solution().buildArray(input)
print(soln)