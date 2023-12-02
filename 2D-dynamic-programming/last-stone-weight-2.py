from math import ceil


def last_stone_weight(stones):
    total_sum = sum(stones)
    target = ceil(total_sum / 2)
    cache = {}

    def dfs(curr_idx, curr_sum):
        if curr_sum >= target or curr_idx >= len(stones):
            second_pile = total_sum - curr_sum
            diff = abs(second_pile - curr_sum)
            return diff

        if (curr_idx, curr_sum) in cache:
            return cache[(curr_idx, curr_sum)]

        # store the min of two choices
        cache[(curr_idx, curr_sum)] = min(dfs(curr_idx + 1, curr_sum), dfs(curr_idx + 1, curr_sum + stones[curr_idx]))

        return cache[(curr_idx, curr_sum)]

    return dfs(0, 0)


res = last_stone_weight([31, 26, 33, 21, 40])
print(res)
