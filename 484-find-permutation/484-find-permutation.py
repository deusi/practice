class Solution:
    # Runtime Complexity: O(n)
    # O(n)
    def findPermutation(self, s: str) -> List[int]:
        perm = []
        dQueue = [1]
        count = 2
        for c in s:
            if c == 'I':
                while dQueue:
                    perm.append(dQueue.pop())
            dQueue.append(count)
            count += 1
        while dQueue:
            perm.append(dQueue.pop())
        return perm