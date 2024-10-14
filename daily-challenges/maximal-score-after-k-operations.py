import heapq


def maximal_score(nums, k):
    max_heap = [-n for n in nums]
    heapq.heapify(max_heap)

    # perform k operations and keep adding the max value to the result and cecil value back to the heap
    score = 0

    for _ in range(k):
        val = heapq.heappop(max_heap)
        score += (-val)
        # add the new ceil value to the heap
        new_val = val // 3
        heapq.heappush(max_heap, new_val)

    return score


res = maximal_score([10, 10, 10, 10, 10], 5)
print(res)
