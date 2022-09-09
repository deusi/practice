class HitCounter:

    def __init__(self):
        self.seconds = []

    def hit(self, timestamp: int) -> None:
        self._last300sec(timestamp)
        if self.seconds and timestamp == self.seconds[-1][0]:
            self.seconds[-1][1] += 1
        else:
            heapq.heappush(self.seconds, [timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        self._last300sec(timestamp)
        hits = 0
        for v in self.seconds:
            hits += v[1]
        return hits
        
    def _last300sec(self, timestamp):
        while self.seconds and self.seconds[0][0] <= timestamp - 300:
            heapq.heappop(self.seconds)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)