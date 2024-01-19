from collections import defaultdict


# recursive solution
def find_max(strs, M, N):
    cache = {}

    def dfs(curr_idx, curr_m, curr_n):
        if curr_idx == len(strs):
            return 0

        if (curr_idx, curr_m, curr_n) in cache:
            return cache[(curr_idx, curr_m, curr_n)]

        # two choices: include or don't include
        m_count, n_count = strs[curr_idx].count('0'), strs[curr_idx].count('1')
        cache[(curr_idx, curr_m, curr_n)] = dfs(curr_idx + 1, curr_m, curr_n)
        if m_count <= curr_m and n_count <= curr_n:
            cache[(curr_idx, curr_m, curr_n)] = max(cache[(curr_idx, curr_m, curr_n)],
                                                    1 + dfs(curr_idx + 1, curr_m - m_count, curr_n - n_count))

        return cache[(curr_idx, curr_m, curr_n)]

    return dfs(0, M, N)


# dp solution
def find_max_2(strs, M, N):
    cache = defaultdict(int)

    for s in strs:
        m_count, n_count = s.count('0'), s.count('1')
        for m in range(M, m_count - 1, -1):
            for n in range(N, n_count - 1, -1):
                cache[(m, n)] = max(cache[(m, n)], 1 + cache[(m - m_count, n - n_count)])

    return cache[(M, N)]


res = find_max(["10", "0001", "111001", "1", "0"], 5, 3)
print(res)
