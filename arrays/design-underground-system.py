class UndergroundSystem:

    def __init__(self):
        # store ids as the key and starting station and time as values
        self.checkin = {}
        # store the start and end station name as key and total time and count as values
        self.checkout = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, end_station: str, t: int) -> None:
        start_station, time = self.checkin[id]
        route = (start_station, end_station)
        if route not in self.checkout:
            self.checkout[route] = [0, 0]
        self.checkout[route][0] += t - time
        self.checkout[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        total_time, count = self.checkout[route]

        return total_time / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
