# dp solution
def min_costs(days, costs):
    cache = {}
    day_pass = [1, 7, 30]

    for i in range(len(days) - 1, -1, -1):
        cache[i] = float('inf')
        for d, c in zip(day_pass, costs):
            # to move to the next valid day pass
            j = i
            while j < len(days) and days[j] < days[i] + d:
                j += 1
            cache[i] = min(cache[i], cache.get(j, 0) + c)

    return cache[0]


# recursive solution
def min_costs_2(days, costs):
    cache = {}
    day_pass = [1, 7, 30]

    def dfs(curr_idx):
        if curr_idx == len(days):
            return 0
        if curr_idx in cache:
            return cache[curr_idx]

        # initialize the current idx in the cache
        cache[curr_idx] = float('inf')

        for d, c in zip(day_pass, costs):
            j = curr_idx
            while j < len(days) and days[j] < days[curr_idx] + d:
                j += 1

            cache[curr_idx] = min(cache[curr_idx], dfs(j) + c)

        return cache[curr_idx]

    return dfs(0)


res = min_costs_2([1, 4, 6, 7, 8, 20], [2, 7, 15])
print(res)
