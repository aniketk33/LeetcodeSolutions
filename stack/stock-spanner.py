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

# Your StockSpanner object will be instantiated, and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
