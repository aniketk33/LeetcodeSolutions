import heapq


def swim_in_rising_water(grid):
    grid_len = len(grid)
    # min heap to store the time, row, and column
    min_heap = [[grid[0][0], 0, 0]]
    # to add the visited coordinates
    visited_positions = {(0, 0)}
    # to traverse the adjacent rows and columns
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while min_heap:
        prev_time, row, column = heapq.heappop(min_heap)

        if row == grid_len - 1 and column == grid_len - 1:
            return prev_time

        for r, c in directions:
            # get the adjacent row and column
            adj_row, adj_col = row + r, column + c
            # boundary case test for row and column
            if (adj_row < 0 or adj_col < 0 or adj_row == grid_len or adj_col == grid_len or
                    (adj_row, adj_col) in visited_positions):
                continue

            # add the adjacent row and column to the visited set
            visited_positions.add((adj_row, adj_col))
            # get the max time between the current and prev time for greedy approach
            max_time = max(prev_time, grid[adj_row][adj_col])
            heapq.heappush(min_heap, [max_time, adj_row, adj_col])


input_grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
res = swim_in_rising_water(input_grid)
print(res)
