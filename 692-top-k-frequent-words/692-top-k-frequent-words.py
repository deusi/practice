class Solution:
    # Runtime Complexity: O(n log n)
    # Space Complexity: O(n)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        maxHeap = []
        for key, val in counter.items():
            heappush(maxHeap, (-val, key))
        heapq.heapify(maxHeap)
        answer = []
        while maxHeap and k > 0:
            answer.append(heapq.heappop(maxHeap)[1])
            k -= 1
        return answer