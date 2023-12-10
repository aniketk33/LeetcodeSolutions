def flip(s):
    cache = {}

    def dfs(curr_idx, is_mono):
        if curr_idx >= len(s):
            return 0

        if (curr_idx, is_mono) in cache:
            return cache[(curr_idx, is_mono)]

        if is_mono and s[curr_idx] == "0":
            # get the min of after flipping and leaving as it is
            cache[(curr_idx, is_mono)] = min(1 + dfs(curr_idx + 1, is_mono=False), dfs(curr_idx + 1, is_mono))
        elif is_mono and s[curr_idx] == "1":
            cache[(curr_idx, is_mono)] = min(1 + dfs(curr_idx + 1, is_mono), dfs(curr_idx + 1, is_mono=False))
        elif not is_mono and s[curr_idx] == "1":
            cache[(curr_idx, is_mono)] = dfs(curr_idx + 1, is_mono)
        else:
            cache[(curr_idx, is_mono)] = 1 + dfs(curr_idx + 1, is_mono)

        return cache[(curr_idx, is_mono)]

    return dfs(0, True)


# optimal solution
def flip_2(s):
    count = 0
    result = 0
    for char in s:
        if char == "1":
            count += 1
        else:
            # get the min of total flips so far and count of 1's
            result = min(1 + result, count)

    return result


res = flip_2("010110")
print(res)
