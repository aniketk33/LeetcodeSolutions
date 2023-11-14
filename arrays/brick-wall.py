from typing import List


def least_bricks(wall: List[List[int]]) -> int:
    num_rows = len(wall)
    # why initialize with 0? when there is only 1 brick in each row, the dict will be empty
    # as we do not count the last brick of the row
    gap_count_dict = {0: 0}

    for brick_row in wall:
        curr_gap_length = 0
        # excluding the last brick
        for brick_len in brick_row[:-1]:
            curr_gap_length += brick_len
            gap_count_dict[curr_gap_length] = 1 + gap_count_dict.get(curr_gap_length, 0)

    min_bricks = num_rows - max(gap_count_dict.values())

    return min_bricks


# input_wall = [[1], [1], [1]]
input_wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
res = least_bricks(input_wall)
print(res)
