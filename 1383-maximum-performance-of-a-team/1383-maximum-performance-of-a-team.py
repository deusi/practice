class Solution:
    # Runtime Complexity: O(n(log n + log k)) - n log n to sort efficiency and n log k to maintain minHeap sorted
    # Space Complexity: O(n + k) - n for sorted array and k for heap
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        performance = 0
        speedSum = 0
        minHeap = []
        es = sorted(zip(efficiency, speed), reverse=True)
        for e, s in es:
            if len(minHeap) >= k:
                speedSum -= heapq.heappop(minHeap)
            heapq.heappush(minHeap, s)
            speedSum += s
            performance = max(performance, speedSum * e)
        return performance % (10**9 + 7)