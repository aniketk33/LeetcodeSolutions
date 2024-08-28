def min_time(colors, needed_time):
    left = result = 0
    right = 1

    while right < len(colors):
        # check if they are the same
        if colors[left] == colors[right]:
            # if the left is smaller than the right, then move both the pointers
            if needed_time[left] < needed_time[right]:
                result += needed_time[left]
                left = right
            else:
                result += needed_time[right]
        else:
            left = right

        right += 1

    return result


res = min_time('aaaabc', [1, 2, 3, 4, 5, 1])
print(res)
