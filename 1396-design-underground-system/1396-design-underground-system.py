class UndergroundSystem:

    def __init__(self):
        self.checkedIn = {}
        self.totalTime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkedIn[id]
        if (startStation, stationName) not in self.totalTime:
            self.totalTime[(startStation, stationName)] = [0, 0]
        self.totalTime[(startStation, stationName)][0] += (t - startTime)
        self.totalTime[(startStation, stationName)][1] += 1
        del self.checkedIn[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.totalTime:
            return 0
        return self.totalTime[(startStation, endStation)][0] / self.totalTime[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)