def simplify(path):
    stack = []
    curr_path = ''
    for char in path + '/':
        # only check when '/' is current value
        if char == '/':
            # pop the directory from the stack when '..' is current value
            if curr_path == '..':
                if stack:
                    stack.pop()
            # add the directory names to the current path
            elif curr_path != '' and curr_path != '.':
                stack.append(curr_path)
            # reset the current path
            curr_path = ''
        else:
            curr_path += char

    return '/' + '/'.join(stack)


res = simplify('/a/./b/../../c/')
print(res)
