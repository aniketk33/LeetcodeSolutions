'''Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.'''

class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        result_arr = []
        for num1 in nums1:
            if num1 not in nums2 or num1 in result_arr:
                continue            
            result_arr.append(num1)
        
        return result_arr

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
Solution().intersection(nums1, nums2)
