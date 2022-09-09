class HitCounter:

    def __init__(self):
        self.seconds = []

    def hit(self, timestamp: int) -> None:
        #self._last300sec(timestamp)
        heapq.heappush(self.seconds, timestamp)

    def getHits(self, timestamp: int) -> int:
        self._last300sec(timestamp)
        hits = 0
        for v in self.seconds:
            hits += 1
        return hits
        
    def _last300sec(self, timestamp):
        while self.seconds and self.seconds[0] <= timestamp - 300:
            heapq.heappop(self.seconds)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)