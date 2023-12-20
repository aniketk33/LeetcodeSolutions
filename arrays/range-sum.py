from typing import List


class NumArray:

    # def __init__(self, nums: List[int]):
    #     self.num_array = nums
    # def sumRange(self, left: int, right: int) -> int:
    #     total_sum = 0
    #     for i in range(left, right + 1):
    #         total_sum += self.num_array[i]
    #
    #     return total_sum
    # optimal solution
    def __init__(self, nums: List[int]):
        self.prefix_arr = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            self.prefix_arr.append(curr_sum)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix_arr[right]
        left_sum = self.prefix_arr[left - 1] if left > 0 else 0

        return right_sum - left_sum

# Your NumArray object will be instantiated, and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
