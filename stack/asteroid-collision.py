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


res = collision([5, 10, -5])
print(res)
