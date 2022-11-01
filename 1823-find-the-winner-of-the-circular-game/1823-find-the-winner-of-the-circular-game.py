class DLL:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
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
            