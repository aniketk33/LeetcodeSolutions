def validate(pushed, popped):
    stack = []
    i = 0

    for num in pushed:
        stack.append(num)

        # check for the last element in the stack and the ith position in the popped array
        while i < len(popped) and stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1

    return not stack


res = validate([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
print(res)
