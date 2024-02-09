def robot(instructions):
    x, y = 0, 0
    # the robot is facing north
    dir_x, dir_y = 0, 1

    for inst in instructions:
        if inst == 'G':
            x, y = x + dir_x, y + dir_y
        # swap the directions
        elif inst == 'L':
            dir_x, dir_y = -1 * dir_y, dir_x
        else:
            dir_x, dir_y = dir_y, -1 * dir_x

    return (x, y) == (0, 0) or (dir_x, dir_y) != (0, 1)


res = robot('GGLLGG')
print(res)
