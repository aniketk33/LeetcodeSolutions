import heapq
from typing import List


# O(nlog(n)) solution
def car_pooling(trips: List[List[int]], capacity: int):
    # sort the array with their starting position
    trips.sort(key=lambda x: x[1])

    min_heap = []  # [end position and passenger count]
    curr_passengers = 0

    for trip in trips:
        passengers, start_position, end_position = trip

        # if the current trip's start position is less than the ongoing end position,
        # then add it to the heap
        while min_heap and start_position >= min_heap[0][0]:
            curr_passengers -= min_heap[0][1]
            heapq.heappop(min_heap)

        curr_passengers += passengers
        if curr_passengers > capacity:
            return False

        heapq.heappush(min_heap, (end_position, passengers))

    return True


# O(n) solution. Brute force solution
def car_pooling_2(trips: List[List[int]], capacity: int):
    # check for the conditions below in the description of the problem
    result = [0] * 1001

    for trip in trips:
        passengers, start_position, end_position = trip
        result[start_position] += passengers
        result[end_position] += passengers

    curr_passengers = 0
    for i in range(1001):
        curr_passengers += result[i]
        if curr_passengers > capacity:
            return False

    return True


res = car_pooling_2([[2, 1, 5], [3, 3, 7]], 4)
print(res)
