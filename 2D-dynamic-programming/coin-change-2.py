def coin_change(coins, amount):
    # NOTE: coins are ROWS and amount range are the COLUMNS
    # target amounts
    bottom_row = [0] * (amount + 1)
    # base case
    bottom_row[0] = 1

    # starting from the last coin
    for row in range(len(coins) - 1, -1, -1):
        curr_row = [0] * (amount + 1)
        # base case
        curr_row[0] = 1
        # these are the range of amounts (column values)
        for curr_amount in range(1, amount + 1):
            # add the bottom value
            curr_row[curr_amount] += bottom_row[curr_amount]
            if curr_amount - coins[row] >= 0:
                # add the right value
                curr_row[curr_amount] += curr_row[curr_amount - coins[row]]

        bottom_row = curr_row

    # at the end, the bottom row will become the top row
    return bottom_row[amount]


res = coin_change([1, 99], 100)
print(res)
