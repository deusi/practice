# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Runtime Complexity: O(max(m, n))
    # Space Complexity: O(n), worst case m = 0
    # Total Time: 13 m
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        sentinel = ListNode(-1, l1)
        prev = sentinel
        while l1 and l2:
            if l2.val < l1.val:
                tmp = l2
                l2 = l2.next
                tmp.next = l1
                prev.next = tmp
            else:
                l1 = l1.next
            prev = prev.next
        if l2:
            prev.next = l2
        return sentinel.next