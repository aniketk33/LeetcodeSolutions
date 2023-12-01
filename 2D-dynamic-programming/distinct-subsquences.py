def distinct_subsquences(s, t):
    cache = {}

    # index values for s and t respectively
    def dfs(left_ptr, right_ptr):
        # there will be a single subsquence is t is empty
        if right_ptr == len(t):
            return 1
        # you cannot make any subsquences from the first string
        if left_ptr == len(s):
            return 0

        if (left_ptr, right_ptr) in cache:
            return cache[(left_ptr, right_ptr)]

        if s[left_ptr] == t[right_ptr]:
            cache[(left_ptr, right_ptr)] = dfs(left_ptr + 1, right_ptr + 1) + dfs(left_ptr + 1, right_ptr)
        else:
            cache[(left_ptr, right_ptr)] = dfs(left_ptr + 1, right_ptr)

        return cache[(left_ptr, right_ptr)]

    return dfs(0, 0)


res = distinct_subsquences('rabbbit', 'rabbit')
print(res)
