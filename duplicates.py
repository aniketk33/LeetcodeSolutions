class Solution:
    def containsDuplicate(self, nums) -> bool:
        # return false when the list is empty
        if nums is None:
            return False
                
        # creating a set to check the existing element present or not
        num_count_set = set()
        
        for i in nums:
            if i in num_count_set:
                # if any of the value is greater than 1 return true
                return True
            num_count_set.add(i)
        return False

# input_list = [1,1,1,3,3,4,3,2,4,2]
input_list = [1,2,3]
soln = Solution().containsDuplicate(input_list)
print(soln)