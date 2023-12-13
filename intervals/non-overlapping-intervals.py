def non_overlapping(intervals):
    intervals.sort()
    overlapping_count = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= prev_end:
            prev_end = end
        else:
            overlapping_count += 1
            # consider only the interval which ends first
            prev_end = min(prev_end, end)

    return overlapping_count


res = non_overlapping([[1, 2], [2, 3]])
print(res)
