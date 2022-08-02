from heapq import *

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heappush(maxHeap, -matrix[i][j])
                if len(maxHeap) > k:
                    heappop(maxHeap)
        return -maxHeap[0]