import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap, self.k = nums, k
        # initialize the heap at the object creation
        heapq.heapify(self.min_heap)
        # pop items until the length of the heap is k. keep only the larger values
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        # remove the smaller value
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]


# valid solution but too expensive for greater array lengths as we have to copy each time we add a new value
class KthLargest_new:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-1 * n for n in nums]

    def add(self, val: int) -> int:
        result = -1
        self.nums.append(-1 * val)
        temp_nums = self.nums.copy()
        temp_k = self.k
        heapq.heapify(temp_nums)
        while temp_k > 0:
            result = heapq.heappop(temp_nums)
            temp_k -= 1

        return result * -1


obj = KthLargest(3, [4, 5, 8, 2])
input_nums = [3, 5, 10, 9, 4]
for i in input_nums:
    print(obj.add(i))

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
