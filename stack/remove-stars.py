def remove_stars(s):
    stack = []

    for char in s:
        if char == '*':
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)


res = remove_stars('erase*****')
print(res)
