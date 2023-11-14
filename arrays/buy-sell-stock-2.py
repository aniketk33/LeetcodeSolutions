def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        # calculate only when the next price is greater than the previous price
        if prices[i] > prices[i - 1]:
            curr_profit = prices[i] - prices[i - 1]
            profit += curr_profit

    return profit


input_prices = [1, 2, 3, 4, 5]
res = max_profit(input_prices)
print(res)
