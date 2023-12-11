def circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    positive_starting_position = 0
    curr_total = 0
    for i in range(len(gas)):
        curr_total += (gas[i] - cost[i])
        if curr_total < 0:
            curr_total = 0
            positive_starting_position = i + 1

    return positive_starting_position


res = circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
print(res)
