'''Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.'''

class Solution:
    def majorityElement(self, nums: list) -> int:
        unique_elements = set(nums)
        val = 1
        unique_elements_dict = {}
        for uq_element in  unique_elements:
            for num in nums:
                if uq_element != num:
                    continue
                unique_elements_dict[uq_element] = val
                val += 1
            val = 1
        majority_element_count = max(unique_elements_dict.values())
        majority_element = list(unique_elements_dict.keys())[list(unique_elements_dict.values()).index(majority_element_count)]

        return majority_element


input = [1,3,3]
Solution().majorityElement(input)