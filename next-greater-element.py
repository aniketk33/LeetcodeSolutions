class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = []
        for num in nums1:
            index = nums2.index(num)
            if index == len(nums2)-1:
                result.append(-1)
                continue
            largest_num = num
            for i in range(index, len(nums2)):
                if nums2[i] > largest_num:
                    largest_num = nums2[i]
            if largest_num == num:
                largest_num = -1
            result.append(largest_num)
        return result
            

nums1 = [4,1,2]
nums2 = [1,3,4,2]
soln = Solution().nextGreaterElement(nums1, nums2)
print(soln)