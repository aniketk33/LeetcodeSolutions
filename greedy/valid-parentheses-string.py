def is_valid(s):
    open_count, close_count = 0, 0
    for char in s:
        if char == '(':
            open_count, close_count = open_count + 1, close_count + 1
        elif char == ')':
            open_count, close_count = open_count - 1, close_count - 1
        else:
            open_count, close_count = open_count - 1, close_count + 1
        # if the closing count is less than zero then return false
        if close_count < 0:
            return False
        if open_count < 0:
            # reset open count
            open_count = 0

    return open_count == 0


res = is_valid('(*))')
print(res)
