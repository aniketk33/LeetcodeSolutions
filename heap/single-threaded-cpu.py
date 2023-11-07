import heapq
from typing import List


def single_threaded_cpu(task_list: List[List[int]]):
    # append each index to the task items
    for i, t in enumerate(task_list):
        t.append(i)

    # sort the task according to the enqueue time
    task_list.sort(key=lambda x: x[0])

    min_heap = []
    result = []
    curr_time = task_list[0][0]
    curr_idx = 0

    # loop until heap in non-empty or tasks are pending
    while min_heap or len(task_list) > curr_idx:
        # add tasks which are less than curr_time
        while curr_idx < len(task_list) and curr_time >= task_list[curr_idx][0]:
            # push processing time and index of a task to the heap
            heapq.heappush(min_heap, [task_list[curr_idx][1], task_list[curr_idx][2]])
            curr_idx += 1

        # if heap is empty then skip to the next processing time
        if not min_heap:
            curr_time = task_list[curr_idx][0]
        else:
            time, idx = heapq.heappop(min_heap)
            curr_time += time
            result.append(idx)

    return result


tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
res = single_threaded_cpu(tasks)
print(res)
