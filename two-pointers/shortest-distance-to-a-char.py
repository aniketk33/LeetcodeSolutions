def shortest_dist(s, c):
    # get all the index position for c
    check_indices = [idx for idx, char in enumerate(s) if char == c]
    result = [0] * len(s)

    for idx, char in enumerate(s):
        min_dist = float('inf')
        for check_index in check_indices:
            min_dist = min(min_dist, abs(idx - check_index))

        result[idx] = min_dist

    return result


# two-pass solution
def shortest_dist_2(s, c):
    result = [float('inf')] * len(s)
    min_dist = len(s) - 1

    # first pass
    for left in range(len(s)):
        if s[left] == c:
            min_dist = 0

        result[left] = min_dist
        min_dist += 1

    # second pass
    # reset the value for minimum distance
    min_dist = len(s) - 1
    for right in range(len(s) - 1, -1, -1):
        if s[right] == c:
            min_dist = 0

        # get the minimum value from the previous pass and current pass
        result[right] = min(result[right], min_dist)
        min_dist += 1

    return result


# res = shortest_dist('loveleetcode', 'e')
res = shortest_dist_2('loveleetcode', 'e')
print(res)
