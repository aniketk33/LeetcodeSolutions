def collision(asteroids):
    stack = []

    for curr_num in asteroids:
        # collision only occurs when the top of the stack is positive and current val is negative
        while stack and curr_num < 0 < stack[-1]:
            if stack[-1] > abs(curr_num):
                curr_num = 0
            elif stack[-1] == abs(curr_num):
                curr_num = 0
                stack.pop()
            else:
                # remove the element if current curr_num is greater than top most value
                stack.pop()
        if curr_num != 0:
            stack.append(curr_num)

    return stack


def collision_2(asteroids):
    result = []

    for asteroid in asteroids:
        # check for collision
        while result and asteroid < 0 < result[-1]:
            # keep popping the element if it is smaller than current val
            if result[-1] < -asteroid:
                result.pop()
                continue
            elif result[-1] == -asteroid:
                result.pop()
            break
        else:
            result.append(asteroid)

    return result


# res = collision([5, 10, -5])
res = collision_2([5, 10, -5])
print(res)
