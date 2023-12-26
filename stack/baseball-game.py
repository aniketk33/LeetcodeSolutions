def points(operations):
    stack = []

    for operation in operations:
        if operation == 'C':
            stack.pop()
        # double the last value in the stack
        elif operation == 'D':
            last_val = stack[-1]
            stack.append(last_val * 2)
        # add the last two values of the stack
        elif operation == '+':
            addition = stack[-1] + stack[-2]
            stack.append(addition)
        else:
            stack.append(int(operation))

    return sum(stack)


res = points(["5", "-2", "4", "C", "D", "9", "+", "+"])
print(res)
