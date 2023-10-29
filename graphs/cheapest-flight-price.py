def cheapest_flight_price(num_flights, flights_arr, source, destination, stops):
    # prices_arr = [float('inf')] * num_flights
    prices_arr = {i: float('inf') for i in range(num_flights)}
    # source flight price will be 0
    prices_arr[source] = 0

    for i in range(stops + 1):
        # store current prices in temp array
        temp_prices = prices_arr.copy()
        for src, dest, price in flights_arr:
            if prices_arr[src] == float('inf'):
                continue
            # calculate the total cost for current path
            curr_dest_price = price + prices_arr[src]
            # if smaller than previous, update with the cheapest price
            if temp_prices[dest] > curr_dest_price:
                temp_prices[dest] = curr_dest_price

        # set new prices
        prices_arr = temp_prices

    return prices_arr[destination] if prices_arr[destination] != float('inf') else -1


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
s = 0
dst = 3
k = 1
res = cheapest_flight_price(n, flights, s, dst, k)
print(res)
