class DLL:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    # Runtime Complexity: O(k*n^2), since we need to remove all but one nodes and also to iterate k elements at a time
    # Space Complexity: O(n) to build a doubly linked list
    # Total Time: 17 m
    def findTheWinner(self, n: int, k: int) -> int:
        first = DLL(1)
        cur = first
        for i in range(2, n+1):
            cur.next = DLL(i, cur)
            cur = cur.next
        cur.next = first
        first.prev = cur
        for _ in range(n-1):
            for _ in range(k):
                first = first.next
            first.prev = first.prev.prev
            first.prev.next = first
        return first.val
            