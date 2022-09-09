class Solution:
    # Runtime Complexity: O(n log n) to sort the list, n to go over every element
    # Space Complexity: O(n), since heap might grow to the size of the entire list if there's only one a
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        minHeap = []
        count = 0
        properties.sort(key = lambda x: (x[0], -x[1]))
        prevAttack = 0
        for a, d in properties:
            if a > prevAttack:
                while minHeap and d > minHeap[0]:
                    count += 1
                    heapq.heappop(minHeap)
                prevAttack = a
            heapq.heappush(minHeap, d)
        return count