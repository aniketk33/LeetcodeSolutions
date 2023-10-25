import collections


def island_count(grid):
    # if grid is empty
    if not grid:
        return 0

    visited_positions = set()
    islands = 0
    ROWS, COLUMNS = len(grid), len(grid[0])

    def bfs(row, col):
        bfs_queue = collections.deque()
        # add the current row and column to the queue and visited position set
        bfs_queue.append((row, col))
        visited_positions.add((row, col))
        # to traverse adjacent nodes. [Bottom, Up, Right, Left]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while bfs_queue:
            r, c = bfs_queue.popleft()
            for adj_row, adj_col in directions:
                row, col = r + adj_row, c + adj_col
                # 1. whether adjacent row and column are in range
                # 2. check whether it is a 1 and not in visited set
                if (row in range(ROWS) and col in range(COLUMNS) and
                        grid[row][col] == '1' and (row, col) not in visited_positions):
                    # add the adjacent positions to the queue
                    visited_positions.add((row, col))
                    bfs_queue.append((row, col))

    for curr_row in range(ROWS):
        for curr_column in range(COLUMNS):
            if grid[curr_row][curr_column] == '1' and (curr_row, curr_column) not in visited_positions:
                # get all the adjacent 1's
                bfs(curr_row, curr_column)
                islands += 1

    return islands


input_grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
res = island_count(input_grid)
print(res)
