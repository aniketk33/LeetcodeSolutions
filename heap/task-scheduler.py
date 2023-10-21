import heapq
from collections import Counter, deque


def task_scheduler(task_arr, n):
    task_count_arr = Counter(task_arr)
    max_heap = [-count for count in task_count_arr.values()]
    heapq.heapify(max_heap)
    # overall time
    time = 0
    # store the task count and idle time
    task_queue = deque()

    while task_queue or max_heap:
        time += 1
        if max_heap:
            task_count = 1 + heapq.heappop(max_heap)
            # we have to skip 0 to the queue
            if task_count:
                task_queue.append([task_count, time + n])
        # check if the idle time is same to the current time, if so then free the task from the queue
        if task_queue and task_queue[0][1] == time:
            first_val = task_queue.popleft()[0]
            heapq.heappush(max_heap, first_val)

    return time


tasks = ["A", "A", "A", "B", "B", "B"]
res = task_scheduler(tasks, 2)
print(res)
