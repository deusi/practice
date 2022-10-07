class Solution:
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