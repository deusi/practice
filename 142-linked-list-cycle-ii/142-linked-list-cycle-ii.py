# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast, slow = head.next.next, head.next
        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next
        if not fast or not fast.next:
            return None
        cur = head
        while cur != slow:
            cur = cur.next
            slow = slow.next
        return slow