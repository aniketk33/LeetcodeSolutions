def car_fleet(target, position, speed):
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []

    for curr_position, s in pair:
        time = (target - curr_position) / s
        stack.append(time)
        if len(stack) >= 2 and stack[-2] >= stack[-1]:
            stack.pop()

    return len(stack)


# optimal solution with O(1) space
def car_fleet_2(target, position, speed):
    # array with position and speed
    pos_speed_arr = [(pos, speed) for pos, speed in zip(position, speed)]
    pos_speed_arr.sort(reverse=True)

    prev_time = 0
    count = 0
    for curr_pos, speed in pos_speed_arr:
        curr_time = (target - curr_pos) / speed
        # if current time is > than prev time, increase the count of fleet cars
        if curr_time > prev_time:
            count += 1
            prev_time = curr_time

    return count


res = car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
print(res)
