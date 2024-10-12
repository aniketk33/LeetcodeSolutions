import heapq


def divide_intervals(intervals):
    intervals.sort()
    heap = []

    for start, end in intervals:
        # compare the start time with heap's first value
        if heap and start > heap[0]:
            heapq.heappop(heap)
        # store the end time
        heapq.heappush(heap, end)

    return len(heap)


res = divide_intervals([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]])
print(res)
