import heapq


# brute force
def max_product(nums):
    nums.sort()
    # if there are negative numbers
    # for the first two negative numbers and last big positive value
    first = nums[0] * nums[1] * nums[-1]

    # last three positive values
    last_three = nums[-1] * nums[-2] * nums[-3]
    if last_three > first:
        return last_three

    return first


# optimal solution
def max_product_2(nums: list):
    # create two heaps, min and max heaps
    # 1. check for the product of two negative values and one positive
    # 2. and the other would be all positives

    max_heap = [-n for n in nums]
    heapq.heapify(max_heap)
    min_heap = nums
    heapq.heapify(min_heap)

    negative_1, negative_2 = heapq.heappop(min_heap), heapq.heappop(min_heap)
    last_positive = -1 * heapq.heappop(max_heap)

    second_last_positive = -1 * heapq.heappop(max_heap)
    third_last_positive = -1 * heapq.heappop(max_heap)

    negatives = negative_1 * negative_2 * last_positive
    positives = last_positive * second_last_positive * third_last_positive

    if negatives > positives:
        return negatives

    return positives


# res = max_product([1, 2, 3, 4])
res = max_product_2([1, 2, 3, 4])
print(res)
