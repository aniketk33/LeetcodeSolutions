def insert_interval(intervals, new_interval):
    result = []
    for i in range(len(intervals)):
        # case 1: if new interval's last value is less than the current interval's first value then added it before the
        # curr interval as well as the remaining intervals and return the result list
        if intervals[i][0] > new_interval[1]:
            result.append(new_interval)
            return result + intervals[i:]
        # case 2: if new interval's first value is greater than the current interval's last value, then add the current
        # interval to the result list as it is not overlapping
        elif intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
        # Case 3: when the new interval is overlapping then find the min of current's and new interval's first value
        # and max of current's and new interval's last value.
        # Do not append it to the list as it may overlap with other intervals so iterating.
        else:
            new_interval = [min(intervals[i][0], new_interval[0]), max(intervals[i][1], new_interval[1])]

    # case 4: append the new interval before returning the list
    result.append(new_interval)
    return result


intervals_arr = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
res = insert_interval(intervals_arr, newInterval)
print(res)
