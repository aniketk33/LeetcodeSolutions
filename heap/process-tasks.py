import heapq


def process_tasks(servers, tasks):
    result = []

    # create available server's heap [weight, idx]
    avail_servers = [(val, idx) for idx, val in enumerate(servers)]
    heapq.heapify(avail_servers)

    # create unavailable server's list [time_when_it_becomes_free, weight, idx]
    # initially all the servers are available
    unavail_servers = []

    curr_time = 0
    for i, task_time in enumerate(tasks):
        curr_time = max(curr_time, i)

        # check if no server is available to process the task then fast-forward the time to the
        # first server in the unavailable server's list
        if not avail_servers:
            curr_time = unavail_servers[0][0]

        # check if any server is going to be free soon from the unavailable server's list
        # and add them to the available server's list
        while unavail_servers and curr_time >= unavail_servers[0][0]:
            free_time, weight, idx = heapq.heappop(unavail_servers)
            heapq.heappush(avail_servers, (weight, idx))

        # mark the free server as busy
        weight, idx = heapq.heappop(avail_servers)
        total_task_time = task_time + curr_time
        heapq.heappush(unavail_servers, (total_task_time, weight, idx))
        result.append(idx)

    return result


res = process_tasks([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1])
print(res)
