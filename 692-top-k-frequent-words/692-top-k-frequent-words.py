class Solution:
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