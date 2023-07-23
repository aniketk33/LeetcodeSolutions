def max_stock_profit(price_arr):
    arr_len = len(price_arr)
    max_profit = 0
    if arr_len <= 1:
        return max_profit
    buy_ptr = 0
    sell_ptr = 1
    while sell_ptr < arr_len:
        curr_profit = price_arr[sell_ptr] - price_arr[buy_ptr]
        if price_arr[buy_ptr] < price_arr[sell_ptr]:
            max_profit = max(max_profit, curr_profit)
        else:
            buy_ptr = sell_ptr
        sell_ptr += 1

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
res = max_stock_profit(prices)
print(res)
