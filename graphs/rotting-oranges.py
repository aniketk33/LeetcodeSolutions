import collections


def rotting_oranges(grid):
    ROWS, COLUMNS = len(grid), len(grid[0])
    time, fresh_oranges = 0, 0
    bfs_queue = collections.deque()

    for row in range(ROWS):
        for column in range(COLUMNS):
            if grid[row][column] == 1:
                fresh_oranges += 1
            # get the position of the rotten orange
            if grid[row][column] == 2:
                bfs_queue.append([row, column])

    # to traverse adjacent nodes. [Bottom, Up, Right, Left]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while bfs_queue and fresh_oranges > 0:
        # loop on all the current oranges in the queue
        for i in range(len(bfs_queue)):
            r, c = bfs_queue.popleft()
            for adj_row, adj_col in directions:
                # get adjacent row and columns
                row, col = r + adj_row, c + adj_col
                if row < 0 or col < 0 or row == ROWS or col == COLUMNS or grid[row][col] != 1:
                    continue
                # mark the fresh orange as rotten and append it to the queue so that
                # the adjacent oranges can be added
                grid[row][col] = 2
                bfs_queue.append([row, col])
                fresh_oranges -= 1

        time += 1

    return time if fresh_oranges == 0 else -1


input_grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
res = rotting_oranges(input_grid)
print(res)
