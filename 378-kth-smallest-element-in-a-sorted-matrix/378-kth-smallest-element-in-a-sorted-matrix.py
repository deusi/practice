from heapq import *

class Solution:
    # Runtime Complexity: O(n^2 * k log k)
    # Space Complexity O(k)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heappush(maxHeap, -matrix[i][j])
                if len(maxHeap) > k:
                    heappop(maxHeap)
        return -maxHeap[0]