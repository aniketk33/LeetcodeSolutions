def valid_newspaper_sections(read_times, total_coworkers, limit):
    curr_coworkers = curr_time = 0
    for read_time in read_times:
        if curr_time + read_time > limit:
            # reset the curr sum and assign the section to co-worker
            curr_time = 0
            curr_coworkers += 1
        curr_time += read_time

    # edge case: say if the curr_time is not reset when it is under limit, we need to assign the last section to a co-worker
    if curr_time != 0:
        curr_coworkers += 1
    return total_coworkers >= curr_coworkers


def newspaper_split(newspapers_read_times, num_coworkers):
    low, high = max(newspapers_read_times), sum(newspapers_read_times)
    result = 0

    while low <= high:
        # this will be the max time of a given coworker
        mid = (low + high) // 2
        if valid_newspaper_sections(newspapers_read_times, num_coworkers, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


res = newspaper_split([7, 2, 5, 10, 8], 2)
print(res)
