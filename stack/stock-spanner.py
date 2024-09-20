class StockSpanner:

    def __init__(self):
        # store the value and span count
        self.stocks = []

    def next(self, price: int) -> int:
        span_count = 1
        while self.stocks and self.stocks[-1][0] <= price:
            _, count = self.stocks.pop()
            span_count += count

        self.stocks.append((price, span_count))

        return span_count

    # this is also a solution but time limits exceeds
    def next_2(self, price):
        count = 1
        n = len(self.stocks)

        for i in range(n - 1, -1, -1):
            if self.stocks[i] > price:
                break
            count += 1

        self.stocks.append(price)
        return count

# Your StockSpanner object will be instantiated, and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
