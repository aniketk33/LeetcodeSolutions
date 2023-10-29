import heapq


def min_distance(points):
    num_points = len(points)

    # create hashmap for all the adjacency points and its manhattan distance
    adjacent_points_dict = {i: [] for i in range(num_points)}
    for point_1 in range(num_points):
        x1, y1 = points[point_1]
        for point_2 in range(point_1 + 1, num_points):
            x2, y2 = points[point_2]
            dist = abs(x1 - x2) + abs(y1 - y2)
            # store the distance and the given point
            adjacent_points_dict[point_1].append([dist, point_2])
            adjacent_points_dict[point_2].append([dist, point_1])

    visited_points = set()
    total_dist = 0
    # initialize the heap with min value
    min_heap = [[0, 0]]

    while len(visited_points) < num_points:
        dist, point = heapq.heappop(min_heap)
        if point in visited_points:
            continue
        total_dist += dist
        visited_points.add(point)

        # loop through its adjacent points and add to the heap
        for neighbor_dist, neighbor_point in adjacent_points_dict[point]:
            if neighbor_point not in visited_points:
                heapq.heappush(min_heap, [neighbor_dist, neighbor_point])

    return total_dist


input_points = [[3, 12], [-2, 5], [-4, 1]]
res = min_distance(input_points)
print(res)
