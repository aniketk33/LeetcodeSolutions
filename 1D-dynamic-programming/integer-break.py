def integer_break(n):
    cache = {1: 1}

    def dfs(curr_num):
        if curr_num in cache:
            return cache[curr_num]

        cache[curr_num] = 0 if curr_num == n else curr_num
        for i in range(1, curr_num):
            val = dfs(i) * dfs(curr_num - i)
            cache[curr_num] = max(cache[curr_num], val)

        return cache[curr_num]

    return dfs(n)


# dp solution
def integer_break_2(n):
    cache = {1: 1}

    for curr_num in range(2, n + 1):
        cache[curr_num] = 0 if curr_num == n else curr_num
        for i in range(1, curr_num):
            val = cache[i] * cache[curr_num - i]
            cache[curr_num] = max(cache[curr_num], val)

    return cache[n]


res = integer_break_2(10)
print(res)
