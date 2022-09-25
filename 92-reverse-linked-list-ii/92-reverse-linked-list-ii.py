# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(cur, to):
            prev = None
            for _ in range(to + 1):
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev, cur
        
        sentinel = ListNode(-1, head)
        lastOrig = sentinel
        count = 1
        while count < left:
            head = head.next
            lastOrig = lastOrig.next
            count += 1
        revNode, afterReverse = reverse(head, right - left)
        lastOrig.next = revNode
        head.next = afterReverse
        return sentinel.next
                
            
            