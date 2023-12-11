from typing import List


def merge_intervals(intervals: List[List[int]]):
    # sort them by their starting value
    intervals.sort(key=lambda x: x[0])
    # add the first interval
    output = [intervals[0]]

    for start, end in intervals:
        prev_end = output[-1][1]
        # check if the previous interval's end value is greater than or equal to the current interval's start value
        # .i.e they are overlapping
        if prev_end >= start:
            output[-1][1] = max(prev_end, end)
        else:
            output.append([start, end])

    return output


res = merge_intervals([[1, 3], [2, 6], [8, 10], [15, 20]])
print(res)
