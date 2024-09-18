def buy_tickets(tickets, k):
    count = 0

    while tickets[k] > 0:
        for i in range(len(tickets)):
            if i == k and tickets[k] <= 0:
                break
            if tickets[i] <= 0:
                continue
            count += 1
            tickets[i] -= 1

    return count


def buy_tickets_2(tickets, k):
    count = 0

    for i, val in enumerate(tickets):
        # if i <= k:
        #     count += min(val, tickets[k])
        # else:
        #     count += min(val, tickets[k] - 1)

        # more efficient
        if i <= k:
            if val <= tickets[k]:
                count += val
            else:
                count += tickets[k]
        else:
            if val <= tickets[k] - 1:
                count += val
            else:
                count += tickets[k] - 1

    return count


# res = buy_tickets([2, 3, 2], 2)
res = buy_tickets_2([2, 3, 2], 2)
print(res)
