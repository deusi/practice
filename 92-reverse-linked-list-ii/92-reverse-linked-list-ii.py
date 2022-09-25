# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Runtime Complexity: O(n) to go over the list
    # Space Complexity: O(1), since we are only chaning pointers
    # Total Time: 24 m
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(cur, to):
            prev = None
            for _ in range(to):
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
        revNode, afterReverse = reverse(head, right - left + 1)
        lastOrig.next = revNode
        head.next = afterReverse
        
        return sentinel.next
                
            
            