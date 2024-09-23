def teemo(time_series, duration):
    count = 0
    # to avoid adding repetitive range to the result, we store the last interval
    last_interval = 0

    for t in time_series:
        interval = t + duration - 1
        if interval < t:
            continue
        if last_interval and last_interval >= t:
            diff = interval - last_interval
        else:
            diff = interval - t + 1
        last_interval = interval
        count += diff

    return count


res = teemo([1, 2], 2)
print(res)
