def make_square(matchsticks):
    result = sum(matchsticks) // 4
    if sum(matchsticks) / 4 != result:
        return False
    # where to place the current matchstick
    decisions = [0] * 4

    matchsticks.sort(reverse=True)

    def backtrack(curr_idx):
        if curr_idx == len(matchsticks):
            return True

        for i in range(4):
            if matchsticks[curr_idx] + decisions[i] > result:
                continue
            decisions[i] += matchsticks[curr_idx]
            if backtrack(curr_idx + 1):
                return True
            decisions[i] -= matchsticks[curr_idx]

        return False

    return backtrack(0)


res = make_square([1, 1, 2, 2, 2])
print(res)
