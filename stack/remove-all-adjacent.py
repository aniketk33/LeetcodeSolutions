def remove_adjacent(s, k):
    # add the char and count
    stack = []
    result = ''

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char, 1])
        # if its count is equal to k, then pop it
        if stack[-1][1] == k:
            stack.pop()

    for char, count in stack:
        result += (char * count)

    return result


res = remove_adjacent('deeedbbcccbdaa', 3)
print(res)
