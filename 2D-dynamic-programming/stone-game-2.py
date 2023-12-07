def stone_game_2(piles):
    cache = {}

    # passing params: is alice's turn?, current index and current pile range
    def dfs(alice, curr_idx, M):
        if curr_idx >= len(piles):
            return 0
        if (alice, curr_idx, M) in cache:
            return cache[(alice, curr_idx, M)]

        result = 0 if alice else float('inf')
        curr_total = 0
        for X in range(1, 2 * M + 1):
            if curr_idx + X > len(piles):
                break
            curr_total += piles[curr_idx + X - 1]
            if alice:
                result = max(result, curr_total + dfs(False, curr_idx + X, max(M, X)))
            else:
                # no need to add the current pile total to Bob's score, as we need the min of his score
                result = min(result, dfs(True, curr_idx + X, max(M, X)))

        cache[(alice, curr_idx, M)] = result
        return result

    return dfs(True, 0, 1)


res = stone_game_2([2, 7, 9, 4, 4])
print(res)
