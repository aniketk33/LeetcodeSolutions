def min_penalty(customers):
    n = len(customers)
    result = float('inf')

    # Prefix and postfix for N's and Y's.
    # The extra zero is to cover the edge case
    prefix_n = [0] * (n + 1)
    postfix_y = [0] * (n + 1)

    for i in range(1, n + 1):
        # it will be the last position's value
        prefix_n[i] = prefix_n[i - 1]
        # only increment, when 'N' is present
        if customers[i - 1] == "N":
            prefix_n[i] += 1

    # same for postfix of Y's
    for i in range(n - 1, -1, -1):
        postfix_y[i] = postfix_y[i + 1]
        if customers[i] == "Y":
            postfix_y[i] += 1

    min_idx = -1
    for idx, val in enumerate(prefix_n):
        # add them up and store the idx of min value of summation
        penalty = prefix_n[idx] + postfix_y[idx]
        if result > penalty:
            result = penalty
            min_idx = idx

    return min_idx


res = min_penalty('YYNY')
print(res)
