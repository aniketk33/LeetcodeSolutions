from collections import deque, defaultdict
from typing import List


def total_time(n: int, headID: int, manager: List[int], informTime: List[int]):
    adjacent_employees = defaultdict(list)

    for i in range(n):
        # assign the manager its employees
        adjacent_employees[manager[i]].append(i)

    max_time = 0
    # a queue with current employee and time
    bfs_queue = deque([(headID, 0)])

    while bfs_queue:
        curr_employee, curr_time = bfs_queue.pop()
        max_time = max(max_time, curr_time)

        # traverse through its adjacent employees
        for emp in adjacent_employees[curr_employee]:
            # add the current time and time taken for the current employee
            bfs_queue.appendleft((emp, curr_time + informTime[curr_employee]))

    return max_time
