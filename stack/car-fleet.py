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


res = car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
print(res)
