import collections
import heapq


def network_delay(time_arr, nodes, given_node):
    # create adjacency list for the neighbor nodes
    adjacent_nodes = collections.defaultdict(list)

    for node, target_node, time in time_arr:
        # append node and time
        adjacent_nodes[node].append([target_node, time])

    visited_nodes = set()
    # create a min heap with time and node as we need to sort it w.r.t time
    min_heap = [[0, given_node]]
    total_min_time = 0

    while min_heap:
        time, node = heapq.heappop(min_heap)
        # multiple nodes can be added
        if node in visited_nodes:
            continue

        visited_nodes.add(node)
        # get total time of the previous node
        total_min_time = max(total_min_time, time)

        for neighbor_node, neighbor_time in adjacent_nodes[node]:
            if neighbor_node not in visited_nodes:
                # total time for this particular path is prev_node's time plus the current time
                total_time = time + neighbor_time
                heapq.heappush(min_heap, [total_time, neighbor_node])

    return total_min_time if len(visited_nodes) == nodes else -1


times = [[1, 2, 1]]
n, k = 2, 1
res = network_delay(times, n, k)
print(res)
