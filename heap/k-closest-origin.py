import heapq
import math
from typing import List


def closest_origin(points: List[List[int]], k: int):
    # create a min heap with distance and the coordinates
    min_heap = []
    for x, y in points:
        distance = x ** 2 + y ** 2
        min_heap.append([distance, x, y])

    heapq.heapify(min_heap)
    result = []
    while k > 0:
        # we need to pop items based on the min distance and take its coordinates
        distance, x, y = heapq.heappop(min_heap)
        result.append([x, y])
        k -= 1

    return result


points_arr = [[0, 1], [1, 0]]
res = closest_origin(points_arr, 2)
print(res)
