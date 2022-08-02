from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heappush(maxHeap, -stone)
        while len(maxHeap) > 1:
            s1, s2 = heappop(maxHeap), heappop(maxHeap)
            if s1 != s2:
                heappush(maxHeap, s1 - s2)
        return 0 if not maxHeap else -maxHeap[0]