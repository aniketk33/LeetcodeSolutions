'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.'''

class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        '''1/ we start by assuming that the first element in the list is 0 and store this in variable zero.
        2/ Then we iterate over the list , and as we find any element that is not zero , we swap it with the last position of zero , and increment zero by 1.
        3/ This approach is followed as the order of Non Zero elements in the list is to be kept same.'''
        zero = 0     # stores the position of 0  
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[zero] = nums[zero],nums[i]
                zero+=1

        print(nums)


input = [0,1,0,3,12]
Solution().moveZeroes(input)
        