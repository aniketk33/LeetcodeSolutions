def ship_packages(weights, days):
    left_ptr, right_ptr = max(weights), sum(weights)
    result = right_ptr

    def valid_capacity(capacity):
        curr_capacity, ships = capacity, 1
        for w in weights:
            # reset variables and increment the count of ships when count is less than 0
            if curr_capacity - w < 0:
                ships += 1
                curr_capacity = capacity
            curr_capacity -= w

        return ships <= days

    while left_ptr <= right_ptr:
        mid = left_ptr + (right_ptr - left_ptr) // 2
        if valid_capacity(mid):
            # store the min capacity (mid-value)
            result = min(result, mid)
            right_ptr = mid - 1
        else:
            left_ptr = mid + 1

    return result


res = ship_packages([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print(res)
