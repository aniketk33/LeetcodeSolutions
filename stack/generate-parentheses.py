def generate_parentheses(n):
    result = []
    stack = []  # to hold the current results

    def dfs(open_count, close_count):
        # return iff these three are equal
        if open_count == close_count == n:
            result.append(''.join(stack))
            return

        # only add '(' when open count is less than n
        if open_count < n:
            stack.append('(')
            dfs(open_count + 1, close_count)
            stack.pop()

        # only add ')' when close_count is less than open_count
        if close_count < open_count:
            stack.append(')')
            dfs(open_count, close_count + 1)
            stack.pop()

    dfs(0, 0)
    return result


res = generate_parentheses(1)
print(res)
