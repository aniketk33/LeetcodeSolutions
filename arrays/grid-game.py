def grid_game(grid):
    columns = len(grid[0])
    result = float('inf')
    # calculate the prefix for both the rows
    row1_prefix, row2_prefix = grid[0].copy(), grid[1].copy()

    for i in range(1, columns):
        row1_prefix[i] += row1_prefix[i - 1]
        row2_prefix[i] += row2_prefix[i - 1]

    for i in range(columns):
        # current value from the top row
        top = row1_prefix[-1] - row1_prefix[i]
        bottom = row2_prefix[i - 1] if i > 0 else 0
        # 2nd robot will maximize its earning from 1st robot's leftover
        second_robot = max(top, bottom)
        result = min(result, second_robot)

    return result


res = grid_game([[2, 5, 4], [1, 5, 1]])
print(res)
