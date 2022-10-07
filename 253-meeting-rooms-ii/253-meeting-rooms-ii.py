class Solution:
    # Runtime Complexity: O(n log n) for sorting
    # Space Complexity: O(n) to maintain heap
    # Total Time: 22 m
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minHeap = []
        intervals.sort()
        heapq.heappush(minHeap, intervals[0][1])
        for s, e in intervals[1:]:
            if s < minHeap[0]:
                heapq.heappush(minHeap, e)
            else:
                heapq.heapreplace(minHeap, e)
        return len(minHeap)